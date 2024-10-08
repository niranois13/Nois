from django.db import models
from django.apps import apps
import uuid, random

class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
        )

    created_at = models.DateTimeField(
        auto_now_add=True
        )

    updated_at = models.DateTimeField(
        auto_now=True
        )

    slug = models.SlugField(
        max_length=6,
        unique=True,
        null=False,
        blank=True
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        while True:
            slug = str(random.randint(100000, 999999))
            if not self.slug_exists(slug):
                return slug

    def slug_exists(self, slug):
        for model in apps.get_models():
            if hasattr(model, 'slug'):
                if model.objects.filter(slug=slug).exists():
                    return True
        return False

    class Meta:
        abstract = True
