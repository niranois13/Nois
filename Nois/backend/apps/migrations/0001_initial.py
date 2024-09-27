# Generated by Django 5.1.1 on 2024-09-26 13:09

import datetime
import django.contrib.gis.db.models.fields
import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='FR')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('NONE', 'none'), ('CLIENT', 'Client'), ('PROFESSIONAL', 'Professional'), ('ADMIN', 'Admin')], default='NONE', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AppointmentLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(default='France', max_length=75)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adresses',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfessionalAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(default='France', max_length=75)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'Professional Address',
                'verbose_name_plural': 'Professional Addresses',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_helper', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
            bases=('apps.user',),
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profession', models.CharField(choices=[('AMP', 'Aide médico-psychologique'), ('ANIMATEUR', 'Animateur.ice'), ('AUTRE', 'Autre'), ('AS', 'Aide soignant.e'), ('ASS', 'Assistant.e de service social'), ('ASSISTANT FAMILIAL', 'Assistant.e familial.e'), ('AVS', 'Auxiliaire de vie sociale'), ('CESF', 'Conseiller.e en économie sociale et familiale'), ('DEES', 'Educateur.ice spécialisé.e'), ('DEME', 'Moniteur.ice éducateur.ice'), ('EJE', 'Educateur.ice de jeunes enfants'), ('ERGO', 'Ergothérapeute'), ('ETS', 'Educateur.ice technique spécialisé.e'), ('KINE', 'Masseur.se-kinésithérapeute'), ('IFSI', 'Infirmier.e'), ('PSYCHOMOT', 'Psychomotricien.ne'), ('PUER', 'Puericulteur.ice'), ('TISF', "Technicien.ne d'intervention sociale et familiale")], default='AUTRE', max_length=55)),
                ('is_mobile', models.BooleanField(default=True)),
                ('intervention_radius', models.PositiveIntegerField(help_text="Rayon d'intervention (km)", validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(200)])),
            ],
            options={
                'verbose_name': 'Professional',
                'verbose_name_plural': 'Professionals',
            },
            bases=('apps.user',),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appntmnt_datetime_start', models.DateTimeField()),
                ('appntmnt_datetime_end', models.DateTimeField()),
                ('appntmnt_status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('MOD PENDING', 'Modification pending'), ('CANCELED', 'Canceled')], default='PENDING', max_length=50)),
                ('apppntmnt_location', models.CharField(choices=[('DOMICILE', 'Adresse du client'), ('CABINET', 'Adresse du professionel'), ('XT', 'Extérieur')], default='', max_length=35)),
                ('custom_location', models.CharField(blank=True, max_length=255, null=True)),
                ('appntmnt_link', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='apps.appointmentlink')),
                ('client_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.clientaddress')),
                ('professional_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.professionaladdress')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
        migrations.AddField(
            model_name='clientaddress',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address_of_client', to='apps.client'),
        ),
        migrations.AddField(
            model_name='appointmentlink',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.client'),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service_name', models.CharField(max_length=40)),
                ('service_description', models.TextField()),
                ('service_category', models.CharField(choices=[('SOIN_ET_HYGIENE', 'Soins et hygiène'), ('ACCOMPAGNEMENT', 'Accompagnement et transport'), ('EDUCATION_ET_LOISIRS', 'Éducation et loisirs'), ('THERAPIE', 'Thérapie et soutien psychologique'), ('ADMINISTRATIF', 'Gestion administrative et financière'), ('VIE_QUOTIDIENNE', 'Assistance à la vie quotidienne'), ('AUTRE', 'Autre')], default='AUTRE', max_length=100)),
                ('custom_service_category', models.CharField(blank=True, max_length=60, null=True)),
                ('professionals', models.ManyToManyField(blank=True, related_name='services', to='apps.professional')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('degree', models.CharField(default='', max_length=100)),
                ('institution', models.CharField(default='', max_length=50)),
                ('year_of_obtention', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2024)])),
                ('document', models.FileField(blank=True, null=True, upload_to='qualifications/')),
                ('is_verified', models.CharField(choices=[('NON', 'Non vérifié'), ('FOURNI', 'Document fourni'), ('VERIF ADMIN', 'Document vérifié par admin')], default='NON', max_length=60)),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualifications', to='apps.professional')),
            ],
            options={
                'verbose_name': 'Qualification',
                'verbose_name_plural': 'Qualifications',
            },
        ),
        migrations.AddField(
            model_name='professionaladdress',
            name='professional',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address_of_professional', to='apps.professional'),
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('availability_start_datetime', models.DateTimeField()),
                ('availability_end_datetime', models.DateTimeField()),
                ('minimum_duration', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('maximum_duration', models.DurationField(blank=True, null=True)),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='apps.professional')),
            ],
            options={
                'verbose_name': 'Availability',
                'verbose_name_plural': 'Availabilities',
            },
        ),
        migrations.AddField(
            model_name='appointmentlink',
            name='professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.professional'),
        ),
    ]
