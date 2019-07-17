from django.urls import path, include
# Urls
from . import analista, profesional
# Views
from Apps.Client.cliente.views.views import Index

app_name = 'cliente'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('analista/', include(analista.urlpatterns)),
    path('profesional/', include(profesional.urlpatterns)),
]
