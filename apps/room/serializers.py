from rest_framework import serializers

from apps.room.models import Room
from apps.office.serializers import OfficeInfoSerializer
from apps.additional.serializers import ResourceInfoSerializer

class RoomSerializer(serializers.ModelSerializer):
    office = OfficeInfoSerializer()
    resources = ResourceInfoSerializer(many=True)
    
    status_display = serializers.CharField(
        source='get_status_display'
    )
    

    class Meta:
        model = Room
        fields = [
            'id' ,'uuid', 'name', 'description', 'office', 'resources', 'location', 'capacity', 'time_global', 'status_display'
        ]

    def validate_capacity(self, value):
        if value <= 1:
            raise serializers.ValidationError(
                "Capacity must be greater than 1"
            )
        return value
