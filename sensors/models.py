from django.db import models
from devices.models import Devices
from django.utils.timezone import now
from datetime import timedelta
# Create your models here.

class Sensors(models.Model):    
    
    # sensor_type, unit, device_id(FK)
    sensor_type = models.CharField(max_length=30)
    unit = models.CharField(max_length=10)
    
    # from which device, it belongs:
    device_id = models.ForeignKey(Devices, on_delete=models.CASCADE)

    # threshold is different for every sensor
    threshold_max_value = models.DecimalField(max_digits=10, decimal_places=3, default=100)
    threshold_min_value = models.DecimalField(max_digits=10, decimal_places=3, default=1)

    buffer_size = models.DecimalField(max_digits=10, decimal_places=3, default=50)

    active_timeout = models.DecimalField(max_digits=10, decimal_places=3, default=500)


    @property
    def sensor_status(self):
        # 'data_set' refers to the Data model entries linked to this sensor 
        last_entry = self.data_set.order_by('-created_at').first()
        
        if not last_entry:
            return "inactive"
        
        # Current time aur last entry ka difference 
        expiry_time = last_entry.created_at + timedelta(seconds=float(self.active_timeout))
        
        if now() < expiry_time:
            return "active"
        return "inactive"
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.device_id}:{self.sensor_type}"