from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role='NONE', **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if role not in dict(User.ROLE_CHOICES).keys():
            raise ValueError("A valid Role must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)

        if password:
            try:
                validate_password(password, user)
            except ValidationError as e:
                raise ValueError(str(e))

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'ADMIN')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('NONE', 'none'),
        ('CLIENT', 'Client'),
        ('PROFESSIONAL', 'Professional'),
        ('ADMIN', 'Admin'),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True
        )
    first_name = models.CharField(
        max_length=30,
        blank=False,
        null=False
        )
    last_name = models.CharField(
        max_length=30,
        blank=False,
        null=False
        )
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        unique=True
        )
    email = models.EmailField(
        unique=True
        )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='NONE'
        )
    is_active = models.BooleanField(
        default=True
        )
    is_staff = models.BooleanField(
        default=False
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
