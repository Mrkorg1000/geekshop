# Generated by Django 2.2.24 on 2021-12-17 18:15

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0012_auto_20211213_1207"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 12, 19, 18, 15, 26, 751450, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
    ]
