from rest_framework import viewsets, filters
from .models import Room
from .serializers import RoomSerializer, OfficeInfoSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['uuid', 'name', 'description', 'stats']
    ordering_fields = ['name']
