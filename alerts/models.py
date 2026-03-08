from django.db import models
from sensors.models import Sensors
from data.models import Data

# Create your models here.

class Alerts(models.Model):
    
    # Foreign keys
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    sensor_data = models.ForeignKey(Data, on_delete=models.CASCADE)
    
    # alert_type, threshold, status
    alert_msg = models.CharField(max_length=100)

    # alert status: not_resolved or resolved:
    status = models.CharField(max_length=30, default="not_resolved")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sensor}:{self.status}"