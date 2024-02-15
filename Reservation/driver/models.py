# # driver/models.py
# from django.db import models
# from accounts.models import UserDriver

# class Driver(models.Model):
#     user = models.OneToOneField(
#         UserDriver,  # แก้ไขนี้
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     address = models.CharField(max_length=255)
#     phone = models.CharField(max_length=15)
#     work_experience = models.CharField(max_length=255)

#     def __str__(self):
#         return f'Driver: {self.user.name}'
    

# from django.db import models
# from accounts.models import UserDriver

# class Vehicle(models.Model):
#     user = models.ForeignKey(UserDriver, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='vehicles/')
#     model = models.CharField(max_length=100)
#     TYPE_CHOICES = (
#         ('Sack', 'แบบรองกระสอบ'),
#         ('Bucket', 'แบบถังอุ้ม'),
#     )
#     type = models.CharField(max_length=10, choices=TYPE_CHOICES)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     province = models.CharField(max_length=100)

#     def __str__(self):
#         return self.model



