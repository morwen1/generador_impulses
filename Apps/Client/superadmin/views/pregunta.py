from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
# Models
from Apps.General.capitulo.models import Pregunta
# Forms
from Apps.General.capitulo.forms import PreguntaForm, PreguntaUpdateForm


class PreguntaList(ListView):
    model = Pregunta
    template_name = 'superadmin/pregunta/index.html'


class PreguntaCreate(CreateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'superadmin/pregunta/new.html'
    success_url = reverse_lazy('admin:pregunta-list')


class PreguntaUpdate(UpdateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'superadmin/pregunta/new.html'
    success_url = reverse_lazy('admin:pregunta-list')

    def get_form_class(self):
        p = self.object
        if p.capitulo and p.capitulo.norma and p.capitulo.norma.ponderada:
            return PreguntaUpdateForm
        return PreguntaForm


class PreguntaDetail(DetailView):
    model = Pregunta
    template_name = 'superadmin/pregunta/show.html'
