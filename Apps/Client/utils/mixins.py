from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
# Functions
from .functions import add_first_phone


class ReverseMultipleInstanceMixin(object):
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, pk=pk)

    def get_context_data(self, **kwargs):
        context = {}
        context.update({'object': self.get_object()})
        context.update({'disponibles': self.second_model.objects.filter(
            **{self.second_model_property + '__isnull': True}
        )})
        context.update({'asignados': self.second_model.objects.filter(
            **{self.second_model_property: self.get_object()}
        )})
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        property = getattr(obj, self.model_property)
        # Get object second models instances list
        obj_properties = property.values_list('pk', flat=True)
        # Recieved form list
        obj_properties_form_list = list(map(int, request.POST.getlist('asignados[]')))
        for item in obj_properties:
            # Comparing lists
            if item not in obj_properties_form_list:
                # If the item does not exist in the list received is disassociated from the instance
                instance = self.second_model.objects.get(pk=item)
                setattr(instance, self.second_model_property, None)
                instance.save()
        for item in request.POST.getlist('disponibles[]'):
            # Set the received list to the instance
            instance = self.second_model.objects.get(pk=item)
            setattr(instance, self.second_model_property, obj)
            instance.save()
        return redirect(self.success_url_name, obj.pk)


class ReverseCreateMixin(object):
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.second_model, pk=pk)

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            obj = self.get_object()
            instance = form.save(commit=False)
            setattr(instance, self.model_property, obj)
            instance.save()
            return redirect(self.success_url_name, obj.pk)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class UserTypeCreateMixin(object):
    def get_context_data(self, **kwargs):
        context = super(UserTypeCreateMixin, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET or None)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET or None)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            person = form.save(commit=False)
            person.usuario = form2.save()
            person.save()
            user_type = self.type_model()
            setattr(user_type, self.type_user_property, person.usuario)
            user_type.save()
            add_first_phone(request.POST.get('telefono'), person)
            if self.add_to_current_user:
                self.request.user.cliente.usuarios.add(person.usuario.pk)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
