from django.db import models
from devices.models import Devices
# Create your models here.

class Sensors(models.Model):    
    
    # sensor_type, unit, device_id(FK)
    sensor_type = models.CharField(max_length=30)
    unit = models.CharField(max_length=10)
    
    # from which device, it belongs:
    device_id = models.ForeignKey(Devices, on_delete=models.CASCADE)

    # threshold is different for every sensor
    threshold_max_value = models.CharField(max_length=30, default=100)
    threshold_min_value = models.CharField(max_length=30, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.device_id}:{self.sensor_type}"
    
    
    
    
    
    