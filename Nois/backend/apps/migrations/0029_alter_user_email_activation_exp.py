# Generated by Django 5.1.1 on 2024-11-06 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0028_alter_user_email_activation_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_activation_exp',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 7, 10, 53, 53, 482337, tzinfo=datetime.timezone.utc)),
        ),
    ]