from django.db import models

# Create your models here.

class Devices(models.Model):
    
    # ID, name, model, location, status
    
    name = models.CharField(max_length=50)
    device_type_id = models.CharField(max_length=100, unique=True)
    
    # LOCATION where device is installed:   (optional)
    location = models.CharField(max_length=50, null=True, blank=True)
    
    @property
    def device_status(self):
        # 'sensors_set' refers to all sensors belonging to this device
        sensors = self.sensors_set.all()
        
        for sensor in sensors:
            if sensor.sensor_status == "active":
                return "active"
        
        return "inactive"

    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name   