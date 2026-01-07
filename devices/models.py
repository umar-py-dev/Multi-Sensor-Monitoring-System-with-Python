from django.db import models

# Create your models here.

class Devices(models.Model):
    
    # ID, name, model, location, status
    
    name = models.CharField(max_length=50)
    device_id = models.CharField(max_length=100, unique=True)
    
    # LOCATION where device is installed:   (optional)
    location = models.CharField(max_length=50, null=True, blank=True)
    
    # Status: for Threshold
    status = models.CharField(max_length=50) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name   