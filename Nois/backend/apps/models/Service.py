from django.db import models
from django.core.exceptions import ValidationError
from .BaseModel import BaseModel


class Service(BaseModel):
    SERVICE_CATEGORY_CHOICES = (
    ("SOIN_ET_HYGIENE", "Soins et hygiène"),
    ("ACCOMPAGNEMENT", "Accompagnement et transport"),
    ("EDUCATION_ET_LOISIRS", "Éducation et loisirs"),
    ("THERAPIE", "Thérapie et soutien psychologique"),
    ("ADMINISTRATIF", "Gestion administrative et financière"),
    ("VIE_QUOTIDIENNE", "Assistance à la vie quotidienne"),
    ("AUTRE", "Autre"),
    )

    service_name = models.CharField(
        max_length=40,
        blank=False,
        null=False
        )

    service_category = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        choices=SERVICE_CATEGORY_CHOICES,
        default="AUTRE"
        )

    custom_service_category = models.CharField(
        max_length=60,
        blank=True,
        null=True
        )

    custom_sevice_is_verified = models.BooleanField(
        default=False
        )

    professionals = models.ManyToManyField(
        'Professional',
        related_name='services',
        blank=True
        )

    def clean(self):
        if self.service_category != "AUTRE" and self.custom_service_category:
            raise ValidationError("Custom category should only be set when 'AUTRE' is selected.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.service_name} ({self.get_service_category_display()})"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ProfessionalService(BaseModel):
    professional = models.ForeignKey('Professional', on_delete=models.CASCADE, related_name='professional_services')
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='professional_services')
    custom_description = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        unique_together = ('professional', 'service')
        verbose_name = 'Professional service description'
        verbose_name_plural= 'Professional services description'

    def __str__(self):
        return f"{self.professional} - {self.service.service_name}"
