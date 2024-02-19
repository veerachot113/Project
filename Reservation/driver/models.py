# driver/models.py
from django.db import models
from accounts.models import UserDriver

    
# class (models.Model):
#     name = models.ForeignKey(UserDriver,on_delete=models.CASCADE)














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


# class Pet(models.Model):
#     name = models.CharField(max_length=300)
#     age = models.IntegerField()
#     profile = models.ImageField(upload_to='pets/',null=True,blank=True)
#     sex = models.CharField(max_length=300)
#     breed = models.CharField(max_length=300)
#     desc = models.TextField()
#     date_time = models.DateTimeField()
#     appear = models.BooleanField(default=True)


#     class Meta:
#         verbose_name = 'สัตว์เลี้ยง'
#         verbose_name_plural = 'รายการสัตว์เลี้ยง'
#         ordering = ['id']


#     def __str__(self) -> str:
#         return f'{self.id}  {self.name}'
    
