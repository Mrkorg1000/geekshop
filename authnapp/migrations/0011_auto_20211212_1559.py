# Generated by Django 2.2.24 on 2021-12-12 15:59

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0010_auto_20211212_1329"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 12, 14, 15, 59, 29, 848964, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
    ]
