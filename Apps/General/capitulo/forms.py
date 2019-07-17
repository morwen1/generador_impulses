from django import forms
# Models
from .models import Capitulo, TipoPregunta, Pregunta


class CapituloForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = ['nombre', 'descripcion']
        widgets = {'descripcion': forms.Textarea(attrs={'class': 'materialize-textarea'})}


class CapituloFormUpdate(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = ['nombre', 'descripcion', 'ponderacion']
        widgets = {'ponderacion': forms.NumberInput(attrs={'max': 100, 'min': 0}),
                   'descripcion': forms.Textarea(attrs={'class': 'materialize-textarea'})}


class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['descripcion', 'sugerencia', 'tipo']
        labels = {'descripcion': 'Pregunta', 'sugerencia': 'Recomendaciones'}
        widgets = {'descripcion': forms.Textarea(attrs={'class': 'materialize-textarea'}),
                   'sugerencia': forms.Textarea(attrs={'class': 'materialize-textarea'})}


class PreguntaUpdateForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['descripcion', 'sugerencia', 'tipo', 'ponderacion']
        labels = {'descripcion': 'Pregunta', 'sugerencia': 'Recomendaciones'}
        widgets = {'ponderacion': forms.NumberInput(attrs={'min': 0, 'max': 100}),
                   'descripcion': forms.Textarea(attrs={'class': 'materialize-textarea'}),
                   'sugerencia': forms.Textarea(attrs={'class': 'materialize-textarea'})}
