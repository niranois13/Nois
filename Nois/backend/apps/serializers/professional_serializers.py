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
            ]

    def create(self, validated_data):
        is_mobile = validated_data.pop('is_mobile')
        intervention_radius = validated_data.pop('intervention_radius')
        profession = validated_data.pop('profession')
        validated_data['role'] = 'PROFESSSIONAL'

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
            **validated_data
        )
        professional.set_password(password)
        professional.save()

        return professional
