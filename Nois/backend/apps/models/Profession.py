from django.db import models
from .BaseModel import BaseModel
from django.core.exceptions import ValidationError
from django.conf import settings

class Profession(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True
        )
    custom_profession = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
        )
    approved = models.BooleanField(
        default=False
        )
    proposed_by = models.CharField(
        blank=True,
        null=True,
    )

    @property
    def proposed_by(self):
        User = settings.AUTH_USER_MODEL
        return User.objects.filter(slug=self.proposed_by).first()

    def __str__(self):
        return f"{self.name} ({'Approved' if self.approved else 'Pending approval'})"

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"
