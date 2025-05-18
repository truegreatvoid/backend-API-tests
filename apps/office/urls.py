from django.urls import include, path
from rest_framework import routers

from apps.office.views import OfficeViewSet


app_name = 'office'

router = routers.DefaultRouter()
router.register(r'api', OfficeViewSet, basename='crud-office')

urlpatterns = [
    path('', include(router.urls)),
]
