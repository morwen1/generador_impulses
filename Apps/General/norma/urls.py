from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Views
from .views import NormaViewSet

app_name = 'norma'

router = DefaultRouter()
router.register('', NormaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
