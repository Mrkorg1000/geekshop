# Generated by Django 2.2.24 on 2021-11-27 20:06

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0004_auto_20211127_2002"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 11, 29, 20, 6, 23, 207809, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
    ]
