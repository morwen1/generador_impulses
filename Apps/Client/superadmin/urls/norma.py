from django.urls import path
# Views
from Apps.Client.superadmin.views.norma import NormaList, NormaCreate, NormaDetail, NormaUpdate, NormaCapitulo, \
    NormaCapituloCreate

urlpatterns = [
    path('', NormaList.as_view(), name='norma-list'),
    path('new/', NormaCreate.as_view(), name='norma-create'),
    path('<int:pk>/', NormaDetail.as_view(), name='norma-detail'),
    path('<int:pk>/edit/', NormaUpdate.as_view(), name='norma-edit'),
    path('<int:pk>/capitulo/', NormaCapitulo.as_view(), name='norma-capitulo'),
    path('<int:pk>/capitulo/new/', NormaCapituloCreate.as_view(), name='norma-capitulo-create'),
]
