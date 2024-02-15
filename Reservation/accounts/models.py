# accounts/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.get_or_create(name='farmer')
    Group.objects.get_or_create(name='driver')

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', 'previous_migration'),
    ]
    operations = [
        migrations.RunPython(create_groups),
    ]

class UserFarmer(AbstractUser):
    # add custom fields for farmer
    groups = models.ManyToManyField(Group, verbose_name="Groups", blank=True, related_name='accounts_farmer_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name="User Permissions", blank=True, related_name='farmer_users_permissions')
    name = models.CharField(max_length=100, default='')  # เพิ่มชื่อ-สกุล
    address = models.CharField(max_length=255, default='')  # เพิ่มที่อยู่
    phone = models.CharField(max_length=15, default='')  # เพิ่มเบอร์โทรศัพท์
    email = models.EmailField(max_length=255, unique=True)  # Keep email field only
    # เอา Username และ Password มาจาก AbstractUser อยู่แล้ว


class UserDriver(AbstractUser):
    # add custom fields for driver
    groups = models.ManyToManyField(Group, verbose_name="Groups", blank=True, related_name='accounts_driver_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name="User Permissions", blank=True, related_name='accounts_driver_user_permissions')
    name = models.CharField(max_length=100, default='')  # เพิ่มชื่อ-สกุล
    address = models.CharField(max_length=255, default='')  # เพิ่มที่อยู่
    phone = models.CharField(max_length=15, default='')  # เพิ่มเบอร์โทรศัพท์
    email = models.EmailField(max_length=255, unique=True)  # Keep email field only
    # เอา Username และ Password มาจาก AbstractUser อยู่แล้ว


