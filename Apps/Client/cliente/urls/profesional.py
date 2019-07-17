from django.urls import path
# Views
from Apps.Client.cliente.views.profesional import ProfesionalList, ProfesionalCreate


urlpatterns = [
    path('', ProfesionalList.as_view(), name='profesional-list'),
    path('new/', ProfesionalCreate.as_view(), name='profesional-create'),
]
