from django.contrib import admin
from django.contrib.auth.models import User
from .models import Warehouse, Vehicle, Notification

admin.site.register(Warehouse)
admin.site.register(Vehicle)
admin.site.register(Notification)

      

# Register your models here.
