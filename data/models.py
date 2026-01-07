from django.db import models
from sensors.models import Sensors

# Create your models here.

class Data(models.Model):
    
    # timestamp, sensor_id, value
    sensor_id = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    
    
    # main data field: 
    value = models.FloatField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'id: {self.sensor_id} val:{self.value}'