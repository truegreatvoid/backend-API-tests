from rest_framework import serializers

from apps.additional.models import Resource


class ResourceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['name', 'description']
