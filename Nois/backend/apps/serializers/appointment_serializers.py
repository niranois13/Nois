from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from ..models import Appointment, Client, Professional, AppointmentLink
from ..serializers import ClientSerializer, ProfessionalSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    client_slug = serializers.CharField(write_only=True)
    professional_slug = serializers.CharField(write_only=True)

    class Meta:
        model = Appointment
        fields = [
            'client_slug',
            'professional_slug',
            'start',
            'end',
            'description',
            'appntmnt_status',
            'appntmnt_location',
            'custom_location',
            'client_address',
            'professional_address',
            'slug'
        ]
        read_only_fields = ['slug', 'client_slug', 'professional_slug']

    def get_client_slug(self, obj):
        client_serializer = ClientSerializer(obj.client)
        client_slug = client_serializer.data.get('slug')
        return client_slug

    def get_professional_slug(self, obj):
        professional_serializer = ProfessionalSerializer(obj.professional)
        professional_slug =  professional_serializer.data.get('slug')
        return professional_slug

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None

        if not user or user.role != 'CLIENT':
            raise PermissionDenied(
                "Seuls les usagers peuvent créer des rendez-vous."
                )

        client = user.client
        professional_slug = validated_data.get('professional_slug')
        try:
            professional = Professional.objects.get(slug=professional_slug)
        except Professional.DoesNotExist:
            raise serializers.ValidationError(
                f"Aucun professionel trouvé avec cet identifiant: {professional_slug}"
                )

        validated_data.pop('professional_slug', None)
        validated_data.pop('client_slug', None)
        validated_data.pop('client_address', None)
        validated_data.pop('professional_address', None)
        validated_data['appntmnt_status'] = 'PENDING'

        appointment_link = AppointmentLink.objects.create(client=client, professional=professional)
        appointment = Appointment.objects.create(appntmnt_link=appointment_link, **validated_data)

        return appointment

    def validate(self, data):
        user = self.context['request'].user
        role = self.context['request'].user.role

        if hasattr(user, role):
            if role == 'CLIENT':
                if 'client_slug' in data:
                    del data['client_slug']

        return data
