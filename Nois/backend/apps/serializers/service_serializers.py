from rest_framework import serializers
from ..models import Service
from ..serializers import ProfessionalSerializer


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            'service_name',
            'service_description',
            'service_category',
            'custom_service_category',
            'slug'
        ]
        read_only_fields = [
            'slug'
        ]

    def validate(self, data):
        if data.get('service_category') != "AUTRE" and data.get('custom_service_category'):
            raise serializers.ValidationError(
                "Custom category should only be set when 'AUTRE' is selected."
            )
        return data
