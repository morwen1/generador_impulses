from rest_framework import serializers
# Models
from .models import Capitulo, Pregunta


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['pk', 'descripcion', 'sugerencia', 'tipo_pregunta', 'ponderacion']


class CapituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capitulo
        fields = ['pk', 'nombre', 'descripcion', 'ponderacion', 'fecha_creacion', 'fecha_edicion']


class CapituloPreguntaSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True)

    class Meta:
        model = Capitulo
        fields = ['pk', 'nombre', 'descripcion', 'ponderacion', 'preguntas', 'fecha_creacion', 'fecha_edicion']
