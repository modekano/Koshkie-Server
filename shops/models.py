import enum
import random
import string

from django.db import models
from django.contrib.auth.models import User


class ShopType(enum.Enum):
    Food = 1
    Groceries = 2
    Pharmacies = 3


def profile_photo_upload(instance, filename):
    res = instance.id.join(random.choices(string.ascii_letters, k=20))
    return 'shops/{0}'.format(res)


class ShopProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    profile_photo = models.ImageField(upload_to=profile_photo_upload)
    name = models.CharField()
    is_active = models.BooleanField()
    is_open = models.BooleanField()
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    shop_type = models.PositiveIntegerField()

    def __str__(self):
        return self.user.__str__()
