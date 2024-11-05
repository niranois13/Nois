# Generated by Django 5.1.1 on 2024-11-04 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_alter_user_email_activation_exp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professionalservice',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='service',
            name='custom_service_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='custom_service_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_name',
            field=models.CharField(choices=[('Coiffure à domicile', 'Coiffure à domicile'), ('Aide à la toilette', 'Aide à la toilette'), ('Massage relaxant', 'Massage relaxant'), ('Transport médical', 'Transport médical'), ('Aide aux courses', 'Aide aux courses'), ('Compagnie à domicile', 'Compagnie à domicile'), ('Cours de musique', 'Cours de musique'), ('Activités manuelles', 'Activités manuelles'), ('Sorties culturelles', 'Sorties culturelles'), ('Psychothérapie', 'Psychothérapie'), ('Groupe de soutien', 'Groupe de soutien'), ('Conseil familial', 'Conseil familial'), ('Gestion de documents', 'Gestion de documents'), ("Aide à la déclaration d'impôts", "Aide à la déclaration d'impôts"), ('Assistance bancaire', 'Assistance bancaire'), ('Aide au repas', 'Aide au repas'), ('Entretien ménager', 'Entretien ménager'), ('Aide aux démarches', 'Aide aux démarches'), ('Autre service', 'Autre service')], max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_activation_exp',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 5, 11, 33, 10, 343414, tzinfo=datetime.timezone.utc)),
        ),
    ]