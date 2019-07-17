from django.urls import path, include
# Urls
from . import norma, capitulo, pregunta, cliente, licencia
# Views
from Apps.Client.superadmin.views.views import Index

app_name = 'superadmin'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('norma/', include(norma.urlpatterns)),
    path('capitulo/', include(capitulo.urlpatterns)),
    path('pregunta/', include(pregunta.urlpatterns)),
    path('cliente/', include(cliente.urlpatterns)),
    path('licencia/', include(licencia.urlspatterns)),
]
