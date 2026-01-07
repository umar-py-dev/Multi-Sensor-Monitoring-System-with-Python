from django.db import models
from sensors.models import Sensors
from data.models import Data

# Create your models here.

class Alerts(models.Model):
    
    # Foreign keys
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    sensor_data = models.ForeignKey(Data, null=True, blank=True, on_delete=models.SET_NULL)
    
    # alert_type, threshold, status
    alert_type = models.CharField(max_length=50)

    # alert status: active or resolved:
    status = models.CharField(max_length=30)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.alert_type