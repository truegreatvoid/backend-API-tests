from rest_framework import viewsets, filters

from apps.office.models import Office
from apps.office.serializers import OfficeSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['uuid', 'name', 'cnpj', 'location', 'phone', 'stats']
    ordering_fields = ['name']
