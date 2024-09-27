from rest_framework import serializers
from ..models import Professional, Address
from .user_serializers import UserSerializer
from .address_serializers import AddressSerializer


class ProfessionalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    address = AddressSerializer()

    class Meta:
        model = Professional
        fields = [
            'id',
            'user',
            'last_name',
            'first_name',
            'phone_number',
            'profession',
            'is_mobile',
            'intervention_radius',
            'address'
            ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        address_data = validated_data.pop('address')

        user = UserSerializer().create(user_data)
        user.role = 'PROFESSIONAL'
        user.save()

        address = Address.objects.create(**address_data)

        professional = Professional.objects.create(user=user, address=address, **validated_data)

        return professional

'''
class ProfessionalAddressSerializer(AddressSerializer):
    class Meta(AddressSerializer.Meta):
        model = ProfessionalAddress
        fields = [
            'street',
            'city',
            'postal_code',
            'country',
            'latitude',
            'longitude',
            'location'
        ]


class ProfessionalRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    address = ProfessionalAddressSerializer()

    class Meta:
        model = Professional
        fields = [
            'user',
            'first_name',
            'last_name',
            'phone_number',
            'profession',
            'is_mobile',
            'intervention_radius',
            'address',
            ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        address_data = validated_data.pop('address')

        user = User.objects.create_user(
            email=user_data['email'],
            password=user_data['password'],
            role='PROFESSIONAL'
            )

        professional = Professional.objects.create(
            user=user, **validated_data
            )

        if address_data:
            ProfessionalAddress.objects.create(
                professional=professional,
                **address_data
                )

        return professional


class ProfessionalListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    address = ProfessionalAddressSerializer(source='address_of_professional', read_only=True)

    class Meta:
        model = Professional
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'profession',
            'address',
            'is_mobile',
            'intervention_radius'
            ]
'''
