# Generated by Django 2.2.24 on 2021-12-12 13:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0009_auto_20211211_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 14, 13, 29, 4, 819426, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
