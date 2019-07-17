from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
# Models
from Apps.General.user.models import Profesional
# Forms
from Apps.General.user.forms import PersonaForm, UserForm
# Mixins
from Apps.Client.utils.mixins import UserTypeCreateMixin


class ProfesionalList(ListView):
    model = Profesional
    template_name = 'cliente/profesional/index.html'

    def get_queryset(self):
        return self.request.user.cliente.usuarios.filter(profesional__isnull=False)


class ProfesionalCreate(UserTypeCreateMixin, CreateView):
    model = PersonaForm
    type_model = Profesional
    type_user_property = 'usuario'
    template_name = 'cliente/profesional/new.html'
    form_class = PersonaForm
    second_form_class = UserForm
    success_url = reverse_lazy('cliente:profesional-list')
    add_to_current_user = True
