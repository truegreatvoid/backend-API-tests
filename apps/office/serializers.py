from rest_framework import serializers

from apps.office.models import Office


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'

    def validate_capacity(self, value):
        if value <= 1:
            raise serializers.ValidationError(
                "Capacity must be greater than 1"
            )
        return value

class OfficeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['uuid', 'name', 'cnpj']
