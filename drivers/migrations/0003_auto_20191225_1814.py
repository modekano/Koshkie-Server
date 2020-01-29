#  Copyright (c) Code Written and Tested by Ahmed Emad in 29/01/2020, 21:28

# Generated by Django 3.0 on 2019-12-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('drivers', '0002_auto_20191216_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofilemodel',
            name='last_time_online',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='driverprofilemodel',
            name='live_location_latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='driverprofilemodel',
            name='live_location_longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='driverprofilemodel',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
