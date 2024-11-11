from ..models import Professional
from ..serializers import UserSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class ProfessionalSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Professional
        fields = UserSerializer.Meta.fields + [
            'is_mobile',
            'intervention_radius',
            'profession',
            'custom_profession',
            'custom_profession_approved'
            ]

    def to_representation(self, instance):
        request = self.context.get('request', None)
        if request is not None:
            user = request.user
        else:
            user = None

        representation = super().to_representation(instance)

        if user is not None:
            if not (user.is_staff or instance == user):
                representation.pop('id', None)
        else:
            representation.pop('id', None)

        if user is not None:
            if not user.is_staff:
                representation.pop('custom_profession_approved', None)
        else:
            representation.pop('custom_profession_approved', None)

        if user is not None:
            if not (user.is_staff or instance == user):
                representation.pop('role', None)
        else:
            representation.pop('role', None)

        return representation

    def create(self, validated_data):
        is_mobile = validated_data.pop('is_mobile')
        intervention_radius = validated_data.pop('intervention_radius')
        profession = validated_data.pop('profession', None)
        if profession == "":
            profession = None
        custom_profession = validated_data.pop('custom_profession', None)
        custom_profession_approved = validated_data.pop('custom_profession_approved')
        validated_data['role'] = 'PROFESSIONAL'

        password = validated_data.pop('password')
        if password:
            try:
                validate_password(password)
            except ValidationError as e:
                raise ValueError(str(e))

        professional = Professional(
            is_mobile=is_mobile,
            intervention_radius=intervention_radius,
            profession=profession,
            custom_profession = custom_profession,
            custom_profession_approved = custom_profession_approved,
            **validated_data
        )
        professional.set_password(password)
        professional.save()

        return professional

    def update(self, instance, validated_data):
        if validated_data.get('profession') == "":
            validated_data['profession'] = None
        return super().update(instance, validated_data)
