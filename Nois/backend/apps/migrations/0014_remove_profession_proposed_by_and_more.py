# Generated by Django 5.1.1 on 2024-11-05 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_alter_profession_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='proposed_by',
        ),
        migrations.AlterField(
            model_name='user',
            name='email_activation_exp',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 2, 8, 17, 737523, tzinfo=datetime.timezone.utc)),
        ),
    ]
