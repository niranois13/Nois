from rest_framework import serializers
from ..models import Service, ProfessionalService


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            'service_name',
            'service_description',
            'service_category',
            'custom_service_category',
            'custom_service_is_verified',
            'slug'
        ]
        read_only_fields = [
            'slug',
            'custom_service_is_verified'
        ]

    def validate(self, data):
        if data.get('service_category') != "AUTRE" and data.get('custom_service_category'):
            raise serializers.ValidationError(
                "Une autre catégorie ne peut être ajoutée que si 'AUTRE' est sélectionné."
            )
        return data

class ProfessionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalService
        fields = ['professional', 'service', 'custom_description']
