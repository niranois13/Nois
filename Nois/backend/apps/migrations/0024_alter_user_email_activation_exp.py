# Generated by Django 5.1.1 on 2024-11-05 23:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0023_alter_user_email_activation_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_activation_exp',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 23, 37, 36, 400266, tzinfo=datetime.timezone.utc)),
        ),
    ]