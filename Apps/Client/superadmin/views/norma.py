from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
# Models
from Apps.General.norma.models import Norma
from Apps.General.capitulo.models import Capitulo
# Form
from Apps.General.norma.forms import NormaForm
from Apps.General.capitulo.forms import CapituloForm, CapituloFormUpdate
# Mixins
from Apps.Client.utils.mixins import ReverseMultipleInstanceMixin, ReverseCreateMixin


class NormaList(ListView):
    model = Norma
    template_name = 'superadmin/norma/index.html'

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('pk')
        return queryset


class NormaCreate(CreateView):
    model = Norma
    form_class = NormaForm
    template_name = 'superadmin/norma/new.html'
    success_url = reverse_lazy('admin:norma-list')


class NormaDetail(DetailView):
    model = Norma
    template_name = 'superadmin/norma/show.html'

    def get_context_data(self, **kwargs):
        context = super(NormaDetail, self).get_context_data(**kwargs)
        if 'capitulos' not in context:
            context['capitulos'] = Capitulo.objects.filter(norma=self.object.pk)
        return context


class NormaUpdate(UpdateView):
    model = Norma
    form_class = NormaForm
    template_name = 'superadmin/norma/new.html'
    success_url = reverse_lazy('admin:norma-list')


class NormaCapitulo(ReverseMultipleInstanceMixin, View):
    model = Norma
    model_property = 'capitulos'
    second_model = Capitulo
    second_model_property = 'norma'
    success_url_name = 'admin:norma-detail'
    template_name = 'superadmin/norma/capitulo.html'


class NormaCapituloCreate(ReverseCreateMixin, CreateView):
    model = Capitulo
    model_property = 'norma'
    second_model = Norma
    success_url_name = 'admin:norma-detail'
    template_name = 'superadmin/norma/capitulo-new.html'

    def get_form_class(self):
        norma = self.get_object()
        if norma.ponderada:
            return CapituloFormUpdate
        return CapituloForm
