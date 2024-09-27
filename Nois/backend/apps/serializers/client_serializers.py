from rest_framework import serializers
from ..models import Client, Address
from .user_serializers import UserSerializer
from .address_serializers import AddressSerializer


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    address = AddressSerializer()

    class Meta:
        model = Client
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'is_helper',
            'phone_number',
            'address',
            ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        address_data = validated_data.pop('address')

        user = UserSerializer().create(user_data)
        user.role = 'CLIENT'
        user.save()

        address = Address.objects.create(**address_data)

        client = Client.objects.create(user=user, address=address, **validated_data)

        return client

'''
class ClientAddressSerializer(AddressSerializer):
    class Meta(AddressSerializer.Meta):
        model = ClientAddress
        fields = [
            'street',
            'city',
            'postal_code',
            'country',
            'latitude',
            'longitude',
            'location',
        ]


class ClientRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    address = ClientAddressSerializer()

    class Meta:
        model = Client
        fields = [
            'user',
            'first_name',
            'last_name',
            'is_helper',
            'phone_number',
            'address',
            ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        address_data = validated_data.pop('address')

        user = User.objects.create_user(
            email=user_data['email'],
            password=user_data['password'],
            role='CLIENT'
            )

        client = Client.objects.create(user=user, **validated_data)

        if address_data:
            ClientAddress.objects.create(client=client, **address_data)

        return client

class ClientListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    address = ClientAddressSerializer(source='address_of_client', read_only=True)

    class Meta:
        model = Client
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'is_helper',
            'phone_number',
            'address',
            ]

class ClientUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer
    address = AddressSerializer

    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'is_helper',
            'phone_number',
            'address',
        ]

    def validate_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('password')
        return super().update(instance, validated_data)
'''
