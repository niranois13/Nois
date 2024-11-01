from django.db import DataError, IntegrityError
import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from dotenv import load_dotenv
from apps.models import Client, Professional, Profession

User = get_user_model()

@pytest.mark.django_db
class TestUserManager:
    def test_create_user(self):
        user = User.objects.create_user(
            email='test@example.com',
            password='v3rySECur3dp_sswrd',
            role='NONE'
        )
        assert user.email == 'test@example.com'
        assert user.role == 'NONE'
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser
        assert not validate_password(user.password)

    def test_create_user_without_email(self):
        with pytest.raises(ValueError, match="Un email doit être fourni."):
            User.objects.create_user(email='', password='sTrongp_ssword123')

    def test_create_user_with_long_email(self):
        with pytest.raises(DataError):
            User.objects.create_user(email='n'*256 + '@example.com', password='sTrongp_ssword123')

    def test_create_user_with_invalid_role(self):
        with pytest.raises(ValueError, match="Un rôle valide doit être sélectionné."):
            User.objects.create_user(email='test@example.com', password='sTrongp_ssword123', role='INVALID')

    def test_create_user_with_weak_password(self):
        with pytest.raises(ValueError):
            User.objects.create_user(email='test@example.com', password='weak', role='CLIENT')

    def test_create_duplicate_user(self):
        User.objects.create_user(email='test@example.com', password='sTrongp_ssword123')
        with pytest.raises(IntegrityError):
            User.objects.create_user(email='test@example.com', password='S3condsTrongp_ssword123')

    def test_user_str_method(self):
        user = User.objects.create_user(email='test@example.com', password='validP_ssword123')
        assert str(user) == 'test@example.com'

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='sTrongp_ssword123'
        )
        assert admin_user.email == 'admin@example.com'
        assert admin_user.role == 'ADMIN'
        assert admin_user.is_active
        assert admin_user.is_staff
        assert admin_user.is_superuser

    def test_create_superuser_with_invalid_is_staff(self):
        with pytest.raises(ValueError, match='Superuser doit avoir is_staff=True.'):
            User.objects.create_superuser(
                email='admin@example.com',
                password='sTrongp_ssword123',
                is_staff=False
            )

    def test_create_superuser_with_invalid_is_superuser(self):
        with pytest.raises(ValueError, match='Superuser doit avoir is_superuser=True.'):
            User.objects.create_superuser(
                email='admin@example.com',
                password='sTrongp_ssword123',
                is_superuser=False
            )

    def test_create_client(self):
        client = Client.objects.create_user(
            email='test@example.com',
            password='v3rySECur3dp_sswrd',
            role='CLIENT',
            is_helper=False
        )
        assert client.email == 'test@example.com'
        assert client.role == 'CLIENT'
        assert client.is_active
        assert not client.is_staff
        assert not client.is_superuser
        assert not validate_password(client.password)
        assert client.is_helper == False

    def test_create_client_without_email(self):
        with pytest.raises(ValueError, match="Un email doit être fourni."):
            Client.objects.create_user(email='', password='sTrongp_ssword123')

    def test_create_client_with_invalid_role(self):
        with pytest.raises(ValueError, match="Un rôle valide doit être sélectionné."):
            Client.objects.create_user(email='test@example.com', password='sTrongp_ssword123', role='INVALID')

    def test_create_client_with_weak_password(self):
        with pytest.raises(ValueError):
            Client.objects.create_user(email='test@example.com', password='weak', role='CLIENT')

    def test_create_professional(self):
        profession = Profession.objects.create(name='Test_profession')

        professional = Professional.objects.create_user(
            email='test@example.com',
            password='v3rySECur3dp_sswrd',
            role='PROFESSIONAL',
            profession=profession,
            is_mobile=False,
            intervention_radius=0
        )
        assert professional.email == 'test@example.com'
        assert professional.role == 'PROFESSIONAL'
        assert professional.is_active
        assert not professional.is_staff
        assert not professional.is_superuser
        assert not validate_password(professional.password)
        assert professional.is_mobile == False
        assert professional.intervention_radius == 0
        assert professional.profession.name == 'Test_profession'

    def test_create_professional_without_email(self):
        with pytest.raises(ValueError, match="Un email doit être fourni."):
            Professional.objects.create_user(email='', password='sTrongp_ssword123', role='PROFESSIONAL', profession='Test_profession', is_mobile=False, intervention_radius=0)

    def test_create_professional_with_invalid_role(self):
        with pytest.raises(ValueError, match="Un rôle valide doit être sélectionné."):
                Professional.objects.create_user(email='test@example.com', password='sTrongp_ssword123', role='INVALID', profession='Test_profession', is_mobile=False, intervention_radius=0)

    def test_create_professional_with_weak_password(self):
        with pytest.raises(ValueError):
            Professional.objects.create_user(email='test@example.com', password='weak', role='PROFSSIONAL', profession='Test_profession', is_mobile=False, intervention_radius=0)

    def test_create_professional_with_invalid_is_mobile(self):
        with pytest.raises(ValueError):
            Professional.objects.create_user(email='test@example.com', password='sTrongp_ssword123', role='PROFESSIONAL', profession='Test_profession', is_mobile='INAVLID', intervention_radius=0)

    def test_create_professional_with_invalid_profession(self):
        with pytest.raises(ValueError):
            Professional.objects.create_user(email='test@example.com', password='sTrongp_ssword123', role='PROFESSIONAL', profession=True, is_mobile=False, intervention_radius=0)

    def test_create_professional_with_dumb_intervention_radius(self):
        with pytest.raises(ValueError):
            Professional.objects.create_user(email='test@example.com', password='sTrongp_ssword123', role='PROFESSIONAL', profession='Test_profession', is_mobile=True, intervention_radius=500)
