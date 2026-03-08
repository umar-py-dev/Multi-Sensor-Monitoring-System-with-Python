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


        try:
            # may cause error:
            max_threshold = sensorId.threshold_max_value
            min_threshold = sensorId.threshold_min_value

            buffer = Decimal('50.0') 

            alertMsg = ''
            alert_status = ''

            if value > max_threshold:
                alertMsg = f'Value is HIGH: {value}{sensorId.unit}. Crossed the Maximum limit of {max_threshold}'
                if value >= max_threshold + buffer:
                    alert_status = "critical"
                else:
                    alert_status = "warning"


            elif value < min_threshold:
                alertMsg = f'Value is LOW: {value}{sensorId.unit}. Below the Minimum limit of {min_threshold}'
                if value <= min_threshold - buffer:
                    alert_status = "critical"
                else:
                    alert_status = "warning"

            

            # agar alertMsg variable me kuch bi aa jye to "alert" ke database me data insert kr du ga
            if alertMsg:
                Alerts.objects.create(
                    sensor = sensorId,
                    sensor_data = instance,
                    alert_msg = alertMsg,
                    status = alert_status
                    )
                
            print("Signals.py : ", alertMsg)

        except Exception as e:
            print(e)

