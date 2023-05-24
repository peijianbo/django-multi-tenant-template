from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('projects', ProjectViewSet, 'projects')

urlpatterns = [
]

urlpatterns += router.urls
