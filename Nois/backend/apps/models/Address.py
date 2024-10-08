from django.db import models
from django.utils.text import slugify
from .BaseModel import BaseModel
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point

class Address(BaseModel):
    street = models.CharField(
        max_length=255,
        blank=False,
        null=False
        )

    city = models.CharField(
        max_length=100,
        blank=False,
        null=False
        )

    postal_code = models.CharField(
        max_length=10,
        blank=False,
        null=False
        )

    country = models.CharField(
        max_length=75,
        blank=False,
        null=False,
        default='France'
        )

    latitude = models.FloatField(
        null=True,
        blank=True
        )

    longitude = models.FloatField(
        null=True,
        blank=True
        )

    location = gis_models.PointField(
        null=True,
        blank=True
        )

    class Meta:
        abstract = True
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"

    def save(self, *args, **kwargs):
        if self.latitude and self.longitude and not self.location:
            self.location = Point(self.longitude, self.latitude)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.street}, {self.postal_code} {self.city}, {self.country}"
