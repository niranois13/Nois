# Generated by Django 5.1.1 on 2024-10-08 07:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='intervention_radius',
            field=models.PositiveIntegerField(default=0, help_text="Rayon d'intervention (km)", validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(200)]),
        ),
    ]