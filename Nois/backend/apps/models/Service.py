from django.db import models
from django.core.exceptions import ValidationError
from .BaseModel import BaseModel


# Si mise à jour dans SERVICE_CATEGORY_CHOICES et/ou SERVICE_NAME_CHOICES, penser à mettre à jour /Nois/frontend/js/services.js
SERVICE_CATEGORY_CHOICES = (
    ("SOIN_ET_HYGIENE", "Soins et hygiène"),
    ("ACCOMPAGNEMENT", "Accompagnement et transport"),
    ("EDUCATION_ET_LOISIRS", "Éducation et loisirs"),
    ("THERAPIE", "Thérapie et soutien psychologique"),
    ("ADMINISTRATIF", "Gestion administrative et financière"),
    ("VIE_QUOTIDIENNE", "Assistance à la vie quotidienne"),
    ("AUTRE", "Autre"),
)


SERVICE_NAME_CHOICES = {
    "SOIN_ET_HYGIENE": ["Coiffure à domicile", "Aide à la toilette", "Massage relaxant"],
    "ACCOMPAGNEMENT": ["Transport médical", "Aide aux courses", "Compagnie à domicile"],
    "EDUCATION_ET_LOISIRS": ["Cours de musique", "Activités manuelles", "Sorties culturelles"],
    "THERAPIE": ["Psychothérapie", "Groupe de soutien", "Conseil familial"],
    "ADMINISTRATIF": ["Gestion de documents", "Aide à la déclaration d'impôts", "Assistance bancaire"],
    "VIE_QUOTIDIENNE": ["Aide au repas", "Entretien ménager", "Aide aux démarches"],
    "AUTRE": ["Autre service"],
}

def get_service_name_choices():
    choices = []
    for category_services in SERVICE_NAME_CHOICES.values():
        choices.extend([(service, service) for service in category_services])
    return choices

class Service(BaseModel):
    service_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        choices=get_service_name_choices(),
        )

    custom_service_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    service_category = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        choices=SERVICE_CATEGORY_CHOICES,
        default="AUTRE"
        )

    custom_service_category = models.CharField(
        max_length=100,
        blank=True,
        null=True
        )

    is_verified = models.BooleanField(
        default=False
        )

    professionals = models.ManyToManyField(
        'Professional',
        related_name='services_list',
        blank=True
        )

    def clean(self):
        if self.service_category != "AUTRE" and self.custom_service_category:
            raise ValidationError("Custom category should only be set when 'AUTRE' is selected.")

        if self.service_category in self.SERVICE_NAME_CHOICES:
            valid_service_names = self.SERVICE_NAME_CHOICES[self.service_category]
            if self.service_name not in valid_service_names and self.service_category != "AUTRE":
                raise ValidationError(
                    f"Le service '{self.service_name}' n'est pas valide pour la catégorie '{self.service_category}'."
                )

        if self.service_category == "AUTRE" and self.service_name == "Autre service":
            if not self.custom_service_name:
                raise ValidationError("Veuillez entrer un nom personnalisé pour le service si 'Autre service' est sélectionné.")
        else:
            self.custom_service_name = None


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.service_name} ({self.get_service_category_display()})"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ProfessionalService(BaseModel):
    professional = models.ForeignKey(
        'Professional',
        on_delete=models.CASCADE,
        related_name='professional_services'
        )

    service = models.ForeignKey(
        'Service',
        on_delete=models.CASCADE,
        related_name='professional_services'
        )

    custom_description = models.TextField(
        blank=True,
        null=True
        )

    class Meta:
        unique_together = ('professional', 'service')
        verbose_name = 'Professional service description'
        verbose_name_plural= 'Professional services description'

    def __str__(self):
        return f"{self.professional} - {self.service.service_name}"
