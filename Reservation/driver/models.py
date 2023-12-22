# driver/models.py
from django.db import models
from accounts.models import UserDriver

def vehicle_image_path(instance, filename):
    # This function generates the file path for the uploaded image
    return f'vehicle_images/{instance.driver.username}/{filename}'

class Vehicle(models.Model):
    driver = models.ForeignKey(UserDriver, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to=vehicle_image_path, null=True, blank=True)

    def __str__(self):
        return f'{self.year} {self.name} {self.model}'
