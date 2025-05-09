from django.urls import include, path
from rest_framework import routers
from .views import RoomViewSet

app_name = 'room'

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet, basename='crud-room')

urlpatterns = [
    path('', include(router.urls)),
]