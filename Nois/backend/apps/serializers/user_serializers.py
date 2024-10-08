from rest_framework import serializers
from django.core.validators import validate_email
from phonenumber_field.serializerfields import PhoneNumberField
from django.core.exceptions import ValidationError
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'slug',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password'
            ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Le prénom ne peut contenir que des lettres.")
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Le nom ne peut contenir que des lettres.")
        return value

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Format d'e-mail invalide.")

        if self.instance:
            if User.objects.filter(email=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Cet e-mail est déjà utilisé.")
        else:
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError("Cet e-mail est déjà utilisé.")

        return value

    def validate_phone_number(self, value):
        if self.instance:
            if User.objects.filter(phone_number=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Ce numéro de téléphone est déjà utilisé.")
        else:
            if User.objects.filter(phone_number=value).exists():
                raise serializers.ValidationError("Ce numéro de téléphone est déjà utilisé.")

        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        if 'phone_number' in validated_data:
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()

        return instance
