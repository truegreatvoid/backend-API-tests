from rest_framework import viewsets, filters

from apps.additional.models import Resource
from apps.additional.serializers import ResourceInfoSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceInfoSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'uuid', 'name', 'description', 'stats']
    ordering_fields = ['name']
