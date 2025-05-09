from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def validate_capacity(self, value):
        if value <= 1:
            raise serializers.ValidationError(
                "A capacidade deve ser maior que 1"
            )
        return value
