#  Copyright (c) Code Written and Tested by Ahmed Emad in 06/01/2020, 16:28

# Generated by Django 3.0 on 2019-12-08 19:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import shops.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('users', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sort', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=shops.models.product_photo_upload)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('base_price', models.FloatField()),
                ('is_available', models.BooleanField(default=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products',
                                               to='shops.ProductCategoryModel')),
            ],
        ),
        migrations.CreateModel(
            name='ShopProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to=shops.models.shop_photo_upload)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('is_open', models.BooleanField(default=True)),
                ('shop_type', models.PositiveIntegerField()),
                ('favourite_user', models.ManyToManyField(to='users.UserProfileModel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile',
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShopReviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('time_stamp', models.DateTimeField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews',
                                           to='shops.ShopProfileModel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='users.UserProfileModel')),
            ],
        ),
        migrations.CreateModel(
            name='ShopAddressModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('building', models.CharField(max_length=255)),
                ('special_notes', models.TextField()),
                ('phone_number', models.BigIntegerField()),
                ('land_line_number', models.BigIntegerField()),
                ('location_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address',
                                              to='shops.ShopProfileModel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('time_stamp', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews',
                                              to='shops.ProductModel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='users.UserProfileModel')),
            ],
        ),
        migrations.AddField(
            model_name='productcategorymodel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products',
                                    to='shops.ShopProfileModel'),
        ),
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('added_price', models.FloatField()),
                ('currency', models.CharField(max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_ons',
                                              to='shops.ProductModel')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='productcategorymodel',
            unique_together={('shop', 'sort')},
        ),
    ]
