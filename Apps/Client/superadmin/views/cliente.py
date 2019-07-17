from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView
# Models
from Apps.General.user.models import Cliente
# Forms
from Apps.General.user.forms import PersonaForm, UserForm
# Mixins
from Apps.Client.utils.mixins import UserTypeCreateMixin


class ClienteList(ListView):
    model = Cliente
    template_name = 'superadmin/cliente/index.html'


class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'superadmin/cliente/show.html'


class ClienteCreate(UserTypeCreateMixin, CreateView):
    model = PersonaForm
    type_model = Cliente
    type_user_property = 'usuario'
    template_name = 'superadmin/cliente/new.html'
    form_class = PersonaForm
    second_form_class = UserForm
    add_to_current_user = False
    success_url = reverse_lazy('admin:cliente-list')

