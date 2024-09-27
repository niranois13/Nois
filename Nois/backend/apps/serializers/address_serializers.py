from rest_framework import serializers
from ..models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'street',
            'city',
            'postal_code',
            'country',
            'latitude',
            'longitude',
            'location',
        ]
        abstract = True
        