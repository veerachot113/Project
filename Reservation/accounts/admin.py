#accounts/admin.py
from django.contrib import admin
from .models import*

admin.site.register(UserFarmer)
admin.site.register(UserDriver)