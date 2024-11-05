from rest_framework import serializers
from ..models import Service, ProfessionalService
from ..serializers import ProfessionalSerializer


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            'service_name',
            'custom_service_name',
            'service_category',
            'custom_service_category',
            'is_verified',
            'slug'
        ]
        read_only_fields = [
            'slug',
            'is_verified',
        ]

    def validate(self, data):
        service_category = data.get('service_category')
        service_name = data.get('service_name')
        custom_service_name = data.get('custom_service_name')
        custom_service_category = data.get('custom_service_category')

        if service_category != "AUTRE" and custom_service_category:
            raise serializers.ValidationError(
                "Une autre catégorie ne peut être ajoutée que si 'AUTRE' est sélectionné."
            )

        if service_category in Service.SERVICE_NAME_CHOICES:
            valid_service_names = Service.SERVICE_NAME_CHOICES[service_category]
            if service_name not in valid_service_names and service_category != "AUTRE":
                raise serializers.ValidationError(
                    f"Le service '{service_name}' n'est pas valide pour la catégorie '{service_category}'."
                )

        if service_category == "AUTRE" and service_name == "Autre service":
            if not custom_service_name:
                raise serializers.ValidationError(
                    "Veuillez entrer un nom personnalisé pour le service si 'Autre service' est sélectionné."
                )

        return data


class ProfessionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalService
        fields = ['professional', 'service', 'custom_description']
