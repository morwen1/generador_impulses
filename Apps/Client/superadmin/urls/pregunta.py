from django.urls import path
# Views
from Apps.Client.superadmin.views.pregunta import PreguntaList, PreguntaCreate, PreguntaUpdate, PreguntaDetail

urlpatterns = [
    path('', PreguntaList.as_view(), name='pregunta-list'),
    path('new/', PreguntaCreate.as_view(), name='pregunta-create'),
    path('<int:pk>/', PreguntaDetail.as_view(), name='pregunta-detail'),
    path('<int:pk>/edit/', PreguntaUpdate.as_view(), name='pregunta-edit'),
]
