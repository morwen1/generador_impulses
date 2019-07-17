from django.urls import path
# Urls
from Apps.Client.analista.views.views import AnalistaIndex

app_name = 'analista'

urlpatterns = [
    path('', AnalistaIndex.as_view(), name='index'),
]
