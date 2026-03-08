from django.db import models
from sensors.models import Sensors
from data.models import Data

# Create your models here.

class Alerts(models.Model):
    
    # Foreign keys
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)

    sensor_type = models.CharField(max_length=30, default='unknown')

    sensor_data = models.DecimalField(max_digits=30, decimal_places=1, default='unknown')

    device_id = models.IntegerField(default=2)

    max_threshold = models.DecimalField(max_digits=30, decimal_places=1, default='unknown')
    min_threshold = models.DecimalField(max_digits=30, decimal_places=1, default='unknown')




    # alert_type, threshold, status
    alert_type = models.CharField(max_length=100, default='unknown')

    # alert status: not_resolved or resolved:
    status = models.CharField(max_length=30, default="critical")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sensor}:{self.status}"