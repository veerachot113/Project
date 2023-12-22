# accounts/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserFarmer(AbstractUser):
    # add custom fields for farmer
    groups = models.ManyToManyField(Group, verbose_name="Groups", blank=True, related_name='farmer_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name="User Permissions", blank=True, related_name='farmer_user_permissions')
    name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=30, unique=True)  # Add username field
    address = models.CharField(max_length=255, default='')   # Add address field

    def __str__(self):
        return f'UserFarmer: {self.name}'

class UserDriver(AbstractUser):
    # add custom fields for driver
    groups = models.ManyToManyField(Group, verbose_name="Groups", blank=True, related_name='driver_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name="User Permissions", blank=True, related_name='driver_user_permissions')
    name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=30, unique=True)  # Add username field
    address = models.CharField(max_length=255, default='')   # Add address field

    def __str__(self):
        return f'UserDriver: {self.name}'
