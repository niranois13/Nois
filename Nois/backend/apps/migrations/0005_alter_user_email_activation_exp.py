# Generated by Django 5.1.1 on 2024-10-10 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_user_email_activation_exp_user_email_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_activation_exp',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 11, 11, 56, 4, 970437, tzinfo=datetime.timezone.utc)),
        ),
    ]
