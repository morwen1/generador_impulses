from django.urls import path
# Views
from Apps.Client.superadmin.views.licencia import PlanList, PlanCreate, LicenciaClienteList, LicenciaClienteDetail, \
    LicenciaClienteCreate

urlspatterns = [
    # Plan
    path('plan/', PlanList.as_view(), name='licencia-plan-list'),
    path('plan/new/', PlanCreate.as_view(), name='licencia-plan-create'),
    # Licencia
    path('', LicenciaClienteList.as_view(), name='licencia-list'),
    path('<int:pk>/', LicenciaClienteDetail.as_view(), name='licencia-detail'),
    path('new/', LicenciaClienteCreate.as_view(), name='licencia-create'),
]
