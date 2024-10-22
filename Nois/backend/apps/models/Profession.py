from django.db import models
from .BaseModel import BaseModel
from django.conf import settings

class Profession(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    approved = models.BooleanField(default=False)
    proposed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='proposed_professions'
    )

    def __str__(self):
        return f"{self.name} ({'Approved' if self.approved else 'Pending approval'})"

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"
