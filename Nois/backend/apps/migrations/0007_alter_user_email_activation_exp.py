# Generated by Django 5.1.1 on 2024-10-11 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_rename_appntmnt_datetime_end_appointment_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_activation_exp',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 12, 11, 5, 29, 593687, tzinfo=datetime.timezone.utc)),
        ),
    ]
