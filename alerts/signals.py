from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver

from data.models import Data
from .models import Alerts

@receiver(post_save, sender=Data)
def auto_add_alerts(sender, instance, created, **kwargs):

    # when a data inserted/created, i will spcify the variables:
    if created:
        

        sensorId = instance.sensor_id
        value = instance.value

        buffer = sensorId.buffer_size
        


        try:
            # may cause error:
            max_threshold = sensorId.threshold_max_value
            min_threshold = sensorId.threshold_min_value

            
            alert_status = ''

            
            if value >= max_threshold + buffer:
                alert_status = "critical"
            elif value <= min_threshold - buffer:
                alert_status = "critical"
            elif value > min_threshold and value < max_threshold:
                pass
            else:
                alert_status = "warning"

            

            # agar alertMsg variable me kuch bi aa jye to "alert" ke database me data insert kr du ga
            if alert_status:
                Alerts.objects.create(
                    sensor = sensorId,
                    sensor_type = sensorId.sensor_type,
                    sensor_data = value,
                    device_id = sensorId.device_id_id,
                    max_threshold = sensorId.threshold_max_value, 
                    min_threshold = sensorId.threshold_min_value,
                    alert_type = sensorId.sensor_type,
                    status = alert_status
                    )
                
            print("Signals.py : ", value , ":", alert_status)

        except Exception as e:
            
            print(e)

