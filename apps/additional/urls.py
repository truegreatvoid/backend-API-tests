from django.urls import include, path
from rest_framework import routers

from apps.additional.views import ResourceViewSet


app_name = 'additional'

router = routers.DefaultRouter()
router.register(r'resources', ResourceViewSet, basename='crud-additional')

urlpatterns = [
    path('', include(router.urls)),
]
