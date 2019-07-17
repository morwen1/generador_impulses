from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, View
# Models
from Apps.General.capitulo.models import Capitulo, Pregunta
# Forms
from Apps.General.capitulo.forms import CapituloForm, CapituloFormUpdate, PreguntaForm, PreguntaUpdateForm
# Mixins
from Apps.Client.utils.mixins import ReverseMultipleInstanceMixin, ReverseCreateMixin


class CapituloList(ListView):
    model = Capitulo
    template_name = 'superadmin/capitulo/index.html'


class CapituloCreate(CreateView):
    model = Capitulo
    form_class = CapituloForm
    template_name = 'superadmin/capitulo/new.html'
    success_url = reverse_lazy('admin:capitulo-list')


class CapituloUpdate(UpdateView):
    model = Capitulo
    form_class = CapituloForm
    template_name = 'superadmin/capitulo/new.html'
    success_url = reverse_lazy('admin:capitulo-list')

    def get_form_class(self):
        if self.object.norma and self.object.norma.ponderada:
            return CapituloFormUpdate
        return self.form_class

    def get_porcentaje_capitulo(self):
        porcentaje = 100
        for item in Capitulo.objects.filter(norma=self.object.norma).exclude(pk=self.object.pk):
            porcentaje -= item.ponderacion
        return porcentaje

    def get_context_data(self, **kwargs):
        context = super(CapituloUpdate, self).get_context_data(**kwargs)
        if self.object.norma and self.object.norma.ponderada:
            context['porcentaje'] = self.get_porcentaje_capitulo()
        return context


class CapituloDetail(DetailView):
    model = Capitulo
    template_name = 'superadmin/capitulo/show.html'

    def get_context_data(self, **kwargs):
        context = super(CapituloDetail, self).get_context_data(**kwargs)
        if 'preguntas' not in context:
            context['preguntas'] = Pregunta.objects.filter(capitulo=self.object)
        return context


class CapituloPregunta(ReverseMultipleInstanceMixin, View):
    model = Capitulo
    model_property = 'preguntas'
    second_model = Pregunta
    second_model_property = 'capitulo'
    success_url_name = 'admin:capitulo-detail'
    template_name = 'superadmin/capitulo/pregunta.html'


class CapituloPreguntaCreate(ReverseCreateMixin, CreateView):
    model = Pregunta
    model_property = 'capitulo'
    second_model = Capitulo
    success_url_name = 'admin:capitulo-detail'
    template_name = 'superadmin/capitulo/pregunta-new.html'

    def get_form_class(self):
        capitulo = self.get_object()
        if capitulo.norma and capitulo.norma.ponderada:
            return PreguntaUpdateForm
        return PreguntaForm
