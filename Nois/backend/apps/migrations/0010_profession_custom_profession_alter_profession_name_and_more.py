# Generated by Django 5.1.1 on 2024-11-03 20:40

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_remove_service_service_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profession',
            name='custom_profession',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profession',
            name='name',
            field=models.CharField(choices=[('AMP', 'Aide médico-psychologique'), ('ANIMATEUR', 'Animateur.ice'), ('AUTRE', 'Autre'), ('AS', 'Aide soignant.e'), ('ASS', 'Assistant.e de service social'), ('ASSISTANT FAMILIAL', 'Assistant.e familial.e'), ('AVS', 'Auxiliaire de vie sociale'), ('CESF', 'Conseiller.e en économie sociale et familiale'), ('DEES', 'Educateur.ice spécialisé.e'), ('DEME', 'Moniteur.ice éducateur.ice'), ('EJE', 'Educateur.ice de jeunes enfants'), ('ERGO', 'Ergothérapeute'), ('ETS', 'Educateur.ice technique spécialisé.e'), ('KINE', 'Masseur.se-kinésithérapeute'), ('IFSI', 'Infirmier.e'), ('PSYCHOMOT', 'Psychomotricien.ne'), ('PUER', 'Puericulteur.ice'), ('TISF', "Technicien.ne d'intervention sociale et familiale")], max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='profession',
            name='proposed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='professional',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='professionals_list', to='apps.service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='professionals',
            field=models.ManyToManyField(blank=True, related_name='services_list', to='apps.professional'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_activation_exp',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 4, 20, 40, 32, 35857, tzinfo=datetime.timezone.utc)),
        ),
    ]
