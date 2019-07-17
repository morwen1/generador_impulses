from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
import datetime
# Models
from Apps.General.licencia.models import Plan, Licencia, LicenciaCliente
from Apps.General.norma.models import Norma
# Forms
from Apps.General.licencia.forms import PlanForm, LicenciaForm, LicenciaClienteForm


class PlanList(ListView):
    model = Plan
    template_name = 'superadmin/licencia/plan/index.html'


class PlanCreate(CreateView):
    model = Plan
    form_class = PlanForm
    template_name = 'superadmin/licencia/plan/new.html'
    success_url = reverse_lazy('admin:licencia-plan-list')


class LicenciaClienteList(ListView):
    model = Licencia
    template_name = 'superadmin/licencia/index.html'


class LicenciaClienteDetail(DetailView):
    model = LicenciaCliente
    template_name = 'superadmin/licencia/show.html'


class LicenciaClienteCreate(CreateView):
    model = LicenciaCliente
    form_class = LicenciaClienteForm
    second_form_class = LicenciaForm
    template_name = 'superadmin/licencia/new.html'
    success_url = reverse_lazy('admin:licencia-list')

    def get_context_data(self, **kwargs):
        context = super(LicenciaClienteCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET or None)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET or None)
        if 'normas' not in context:
            context['normas'] = Norma.objects.all()
        if 'planes' not in context:
            context['planes'] = Plan.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            licencia = form2.save(commit=False)
            licencia.fecha_vencimiento = datetime.date.today()
            licencia.save()
            licencia_cliente = form.save(commit=False)
            for item in request.POST.getlist('norma[]'):
                licencia_cliente.pk = None
                licencia_cliente.plan = Plan.objects.get(pk=1)
                licencia_cliente.licencia = licencia
                licencia_cliente.norma = Norma.objects.get(pk=item)
                licencia_cliente.save()
            return redirect('admin:licencia-list')



