# Generated by Django 3.0 on 2020-01-06 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0011_auto_20200106_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopaddressmodel',
            name='location_latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)]),
        ),
        migrations.AlterField(
            model_name='shopaddressmodel',
            name='location_longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)]),
        ),
    ]
