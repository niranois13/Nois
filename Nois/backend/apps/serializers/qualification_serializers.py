from rest_framework import serializers
from ..models import Qualification

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = [
            'degree',
            'institution',
            'year_of_obtention',
            'is_verified',
            'document',
            'slug'
        ]
        read_only_fields = [
            'is_verified',
            'slug'
        ]
