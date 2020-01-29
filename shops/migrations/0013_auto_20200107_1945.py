# Generated by Django 3.0 on 2020-01-07 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0012_auto_20200106_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopprofilemodel',
            name='vat',
            field=models.FloatField(default=0, max_length=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
