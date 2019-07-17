from django import forms
# Models
from .models import Plan, Licencia, LicenciaCliente


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'


class LicenciaForm(forms.ModelForm):
    class Meta:
        model = Licencia
        fields = ['analistas', 'profesionales', 'duracion']
        labels = {'duracion': 'Duración (dias):'}
        widgets = {'analistas': forms.TextInput(attrs={'style': 'pointer-events: none;'})}


class LicenciaClienteForm(forms.ModelForm):
    class Meta:
        model = LicenciaCliente
        fields = ['cliente']
