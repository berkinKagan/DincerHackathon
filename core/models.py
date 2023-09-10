from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from django.contrib.auth import get_user_model

# Create your models here.

WAREHOUSE_GOOD_LIST =[
    ("Refgerator"),
    ("Television"),
    ("Mobile Phone"),
    ("Game Console"),
    ("Computer")
]

VEHICLE_GOOD_LIST = [
    ("Refgerator"),
    ("Television"),
    ("Mobile Phone")
]

User = get_user_model()


    
class Warehouse(models.Model):
    name = models.CharField(max_length=100000, default="")
    adress = models.CharField(max_length=100000, default="")
    solidityRatio = models.FloatField(blank=False, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    segmentedImage = models.ImageField(upload_to = 'images', default = 'default-profile-image-png-1-Transparent-Images.png', null=True)
    normalImage = models.ImageField(upload_to = 'images', default = 'default-profile-image-png-1-Transparent-Images.png', null=True)
    
    def __str__(self):
        return self.name
    
    
class Vehicle(models.Model):
    name = models.CharField(max_length=100000, default="")
    solidityRatio = models.FloatField(blank=False, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=0)
    
    def __str__(self):
        return self.name
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=0)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100000000000, default="")
    shelf = models.CharField(max_length=100, default="")
    good_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.name
                    