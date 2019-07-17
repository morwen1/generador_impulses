from django import forms
# Models
from .models import Norma


class NormaForm(forms.ModelForm):
    class Meta:
        model = Norma
        fields = ['descripcion', 'ponderada']
        labels = {'ponderada': 'Tipo de Norma:'}
        widgets = {
            'ponderada': forms.RadioSelect(choices=[
                (True, 'Ponderada'),
                (False, 'No Ponderada'),
            ])
        }


