from django.urls import path
# Views
from Apps.Client.cliente.views.analista import AnalistaCreate, AnalistaList

urlpatterns = [
    path('', AnalistaList.as_view(), name='analista-list'),
    path('new/', AnalistaCreate.as_view(), name='analista-create'),
]
