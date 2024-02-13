# farmer/models.py
from django.db import models
from accounts.models import UserFarmer  # แก้ไขนี้

class Farmer(models.Model):
    user = models.OneToOneField(
        UserFarmer,  # แก้ไขนี้
        on_delete=models.CASCADE,
        primary_key=True,
    )
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'Farmer: {self.user.name}'

