# Generated by Django 3.0 on 2020-01-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0020_auto_20200120_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optiongroupmodel',
            name='sort',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='optionmodel',
            name='sort',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='productgroupmodel',
            name='sort',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
