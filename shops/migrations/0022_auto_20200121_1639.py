# Generated by Django 3.0 on 2020-01-21 16:39

from django.db import migrations, models
import shops.models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0021_auto_20200121_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='photo',
            field=models.ImageField(default=None, upload_to=shops.models.product_photo_upload),
            preserve_default=False,
        ),
    ]
