from ..models import Client
from ..serializers import UserSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class ClientSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Client
        fields = UserSerializer.Meta.fields + ['is_helper']

    def create(self, validated_data):
        is_helper = validated_data.pop('is_helper', False)
        validated_data['role'] = 'CLIENT'

        password = validated_data.pop('password')
        if password:
            try:
                validate_password(password)
            except ValidationError as e:
                raise ValueError(str(e))

        client = Client(
            is_helper=is_helper,
            **validated_data
        )
        client.set_password(password)
        client.save()

        return client
