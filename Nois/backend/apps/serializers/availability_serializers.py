from rest_framework import serializers
from ..models import Availability

class AvailabilitySerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(source='availability_start_datetime')
    end = serializers.DateTimeField(source='availability_end_datetime')
    title = serializers.CharField(source='availability_title')

    class Meta:
        model = Availability
        fields = [
            'professional',
            'start',
            'end',
            'title',
            'minimum_duration',
            'maximum_duration',
            'slug'
        ]
        read_only_fields = [
            'professional',
            'slug'
        ]

    def create(self, validated_data):
        validated_data['professional'] = self.context['request'].user.professional
        return super().create(validated_data)
