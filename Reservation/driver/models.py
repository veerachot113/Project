# driver/models.py
from accounts.models import UserDriver  # Import the UserDriver model from the accounts app
from django.db import models

class Vehicle(models.Model):
    driver = models.ForeignKey(UserDriver, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'
