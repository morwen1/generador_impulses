from django import forms
from django.contrib.auth.forms import UserCreationForm
# Models
from django.contrib.auth.models import User
from .models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula', 'genero', 'email']
        widgets = {
            'genero': forms.Select(choices=[
                ('M', 'Masculino'),
                ('F', 'Femenino'),
            ]),
            'apellido': forms.TextInput(attrs={'required': 'required'})
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', ]
        help_texts = {
            'username': None,
        }

