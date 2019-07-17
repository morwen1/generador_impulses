from rest_framework import viewsets
# Model
from .models import Norma
# Serializers
from .serializers import NormaSerializer, NormaCapituloSerializer


class NormaViewSet(viewsets.ModelViewSet):
    serializer_class = NormaSerializer
    queryset = Norma.objects.all().order_by('-pk')
    authentication_classes = []

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return NormaCapituloSerializer
        return NormaSerializer
