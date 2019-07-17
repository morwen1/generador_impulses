from django.urls import path
# Views
from Apps.Client.superadmin.views.capitulo import CapituloList, CapituloCreate, CapituloDetail, CapituloUpdate, \
    CapituloPregunta, CapituloPreguntaCreate

urlpatterns = [
    path('', CapituloList.as_view(), name='capitulo-list'),
    path('new/', CapituloCreate.as_view(), name='capitulo-create'),
    path('<int:pk>/', CapituloDetail.as_view(), name='capitulo-detail'),
    path('<int:pk>/edit/', CapituloUpdate.as_view(), name='capitulo-edit'),
    path('<int:pk>/pregunta/', CapituloPregunta.as_view(), name='capitulo-pregunta'),
    path('<int:pk>/pregunta/new/', CapituloPreguntaCreate.as_view(), name='capitulo-pregunta-create'),
]
