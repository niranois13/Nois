from django.db import models
from .Address import Address
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from .UserManager import User

User = get_user_model()

class Professional(User):
    PROFESSION_CHOICES = (
        ("AMP", "Aide médico-psychologique"),
        ("ANIMATEUR", "Animateur.ice"),
        ("AUTRE", "Autre"),
        ("AS", "Aide soignant.e"),
        ("ASS", "Assistant.e de service social"),
        ("ASSISTANT FAMILIAL", "Assistant.e familial.e"),
        ("AVS", "Auxiliaire de vie sociale"),
        ("CESF", "Conseiller.e en économie sociale et familiale"),
        ("DEES", "Educateur.ice spécialisé.e"),
        ("DEME", "Moniteur.ice éducateur.ice"),
        ("EJE", "Educateur.ice de jeunes enfants"),
        ("ERGO", "Ergothérapeute"),
        ("ETS", "Educateur.ice technique spécialisé.e"),
        ("KINE", "Masseur.se-kinésithérapeute"),
        ("IFSI", "Infirmier.e"),
        ("PSYCHOMOT", "Psychomotricien.ne"),
        ("PUER", "Puericulteur.ice"),
        ("TISF", "Technicien.ne d'intervention sociale et familiale"),
    )

    profession = models.CharField(
        max_length=55,
        choices=PROFESSION_CHOICES,
        default="AUTRE",
        blank=False,
        null=False
        )
    is_mobile = models.BooleanField(
        blank=False,
        null=False,
        default=True
        )
    intervention_radius = models.PositiveIntegerField(
            validators=[MinValueValidator(1), MaxValueValidator(200)],
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
