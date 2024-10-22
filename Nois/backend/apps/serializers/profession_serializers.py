from rest_framework import serializers
from ..models import Profession

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = [
            'name',
            'approved',
            'proposed_by',
            'slug'
        ]
        read_only_fields = [
            'approved',
            'proposed_by',
            'slug'
        ]

