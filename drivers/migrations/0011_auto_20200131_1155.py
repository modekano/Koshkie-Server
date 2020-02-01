#  Copyright (c) Code Written and Tested by Ahmed Emad in 31/01/2020, 17:29

# Generated by Django 3.0 on 2020-01-31 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('drivers', '0010_auto_20200125_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofilemodel',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='driverreviewmodel',
            name='sort',
            field=models.PositiveIntegerField(),
        ),
    ]