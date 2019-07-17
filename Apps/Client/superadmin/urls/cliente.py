from django.urls import path
# Views
from Apps.Client.superadmin.views.cliente import ClienteList, ClienteDetail, ClienteCreate

urlpatterns = [
    path('', ClienteList.as_view(), name='cliente-list'),
    path('<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
    path('new/', ClienteCreate.as_view(), name='cliente-create'),
]
