from django.db import models
from .BaseModel import BaseModel
from .Professional import Professional
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Qualification(BaseModel):
    VERIFICATION_STATUS = (
        ('NON', 'Non vérifié'),
        ('FOURNI', 'Document fourni'),
        ('VERIF ADMIN', 'Document vérifié par admin'),
        #('VERIFDIPLOMA', 'Document vérifié par VeriDiploma'),
    )
    degree = models.CharField(max_length=100, blank=False, null=False, default="")
    institution = models.CharField(max_length=50, blank=False, null=False, default="")
    year_of_obtention = models.PositiveIntegerField(validators=[MinValueValidator(1950), MaxValueValidator(timezone.now().year)])
    document = models.FileField(upload_to='qualifications/', null=True, blank=True)
    is_verified = models.CharField(max_length=60, choices=VERIFICATION_STATUS, default='NON')
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='qualifications')

    def __str__(self):
        return f"{self.degree} - {self.professional.first_name} {self.professional.last_name}"

    class Meta:
        verbose_name = "Qualification"
        verbose_name_plural = "Qualifications"

