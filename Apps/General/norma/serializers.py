from rest_framework import serializers
# Models
from .models import Norma
# Serializers
from Apps.General.capitulo.serializers import CapituloPreguntaSerializer


class NormaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Norma
        fields = ['pk', 'descripcion', 'ponderada', 'fecha_creacion', 'fecha_edicion']
        read_only_fields = ['pk', 'fecha_creacion', 'fecha_edicion']


class NormaCapituloSerializer(serializers.ModelSerializer):
    capitulos = CapituloPreguntaSerializer(many=True)

    class Meta:
        model = Norma
        fields = ['pk', 'descripcion', 'ponderada', 'capitulos', 'fecha_creacion', 'fecha_edicion']
