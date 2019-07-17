from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
# Models
from Apps.General.user.models import Analista
# Forms
from Apps.General.user.forms import PersonaForm, UserForm
# Mixins
from Apps.Client.utils.mixins import UserTypeCreateMixin


class AnalistaList(ListView):
    model = Analista
    template_name = 'cliente/analista/index.html'

    def get_queryset(self):
        # return Analista.objects.filter(usuario__cliente=self)
        return self.request.user.cliente.usuarios.filter(analista__isnull=False)


class AnalistaCreate(UserTypeCreateMixin, CreateView):
    model = PersonaForm
    type_model = Analista
    type_user_property = 'usuario'
    template_name = 'cliente/analista/new.html'
    form_class = PersonaForm
    second_form_class = UserForm
    success_url = reverse_lazy('cliente:analista-list')
    add_to_current_user = True
