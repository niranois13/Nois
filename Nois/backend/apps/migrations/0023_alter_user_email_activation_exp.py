# Generated by Django 5.1.1 on 2024-11-05 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0022_alter_profession_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_activation_exp',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 23, 28, 11, 520625, tzinfo=datetime.timezone.utc)),
        ),
    ]
