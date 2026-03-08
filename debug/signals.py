from django.db.models.signals import post_save
from django.dispatch import receiver

from data.models import Data
from .models import DebugLog

@receiver(post_save, sender=Data)
def auto_add_alerts(sender, instance, created, **kwargs):

    # when a data inserted/created, i will spcify the variables:
    if created:
        

        sensorId = instance.sensor_id
        value = instance.value

        
        try:
            print("Debug object Created")
        except Exception as e:
            
            print(e)

