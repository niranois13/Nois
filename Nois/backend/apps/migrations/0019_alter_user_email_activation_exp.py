# Generated by Django 5.1.1 on 2024-11-05 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0018_alter_user_email_activation_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_activation_exp',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 10, 39, 41, 374905, tzinfo=datetime.timezone.utc)),
        ),
    ]