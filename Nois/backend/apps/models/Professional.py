from django.db import models
from .Address import Address
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from .UserManager import User
from .Service import Service

User = get_user_model()

class Professional(User):
    profession = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True
        )
    custom_profession = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
        )
    custom_profession_approved = models.BooleanField(
        default=False
        )
    services = models.ManyToManyField(
        Service,
        related_name='professionals_list',
        blank=True,
        )
    is_mobile = models.BooleanField(
        blank=False,
        null=False,
        default=True
        )
    intervention_radius = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(200)],
        default=0,
        help_text="Rayon d'intervention (km)"
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Professional"
        verbose_name_plural = "Professionals"


class ProfessionalAddress(Address):
    professional = models.OneToOneField(
        Professional,
        on_delete=models.CASCADE,
        related_name='address_of_professional'
        )

    def __str__(self):
        return f"Address of \
            {self.professional.first_name} {self.professional.last_name}"

    class Meta:
        verbose_name = 'Professional Address'
        verbose_name_plural = 'Professional Addresses'
