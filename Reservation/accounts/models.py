from django.db import models

class Farmer(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)