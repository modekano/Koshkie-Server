# Generated by Django 3.0 on 2019-12-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191228_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddressmodel',
            name='type',
            field=models.CharField(choices=[('h', 'house'), ('o', 'office'), ('a', 'apartment')], max_length=1),
        ),
    ]
