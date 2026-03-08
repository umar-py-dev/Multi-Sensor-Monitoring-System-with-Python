from os import environ
import sys
from django import setup
import paho.mqtt.client as mqtt
import json

sys.path.append('/backend/backend/')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings') # django ki settings bhi to dikhani hen is script ko...
setup() # django.setup()

from data.models import Data
from sensors.models import Sensors
from debug.models import DebugLog
from devices.models import Devices

def on_message(client, userdata, msg):
    msg_payload = None
    try:
        # my topic pattern edgef/device/1/sensor/3/data
        topic_parts = msg.topic.split('/')
        sens_id_in_topic = topic_parts[4]
        
        # recreate the topic
        device_id_in_topic = topic_parts[2]
        device_object = Devices.objects.filter(id=device_id_in_topic).first()
        devic_type = device_object.device_type_id

        topic_parts[2] = devic_type
        topic_to_insert = '/'.join(topic_parts)
        
        msg_payload = json.loads(msg.payload.decode())
        value_to_insert = msg_payload.get('value')
        
        sensor_obj = Sensors.objects.filter(id = sens_id_in_topic).first() # chota sa filter
        
        Data.objects.create(sensor_id = sensor_obj, value = value_to_insert)

        DebugLog.objects.create(
            payload = msg_payload,
            topic = topic_to_insert,
            response = 'Data Inserted Successfully',
        )
        
        print(f'Saved value: {value_to_insert} in Sensor id: {str(sensor_obj)}, ')
    
    
    except Exception as err:

        DebugLog.objects.create(
            topic = topic_to_insert,
            payload = msg_payload if msg_payload else {},
            response = err
        )
        print(f"MQTT subscription Error: {err}")
        
    
        
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_message = on_message


client.connect('localhost', 1883, 60)

client.subscribe('edgef/device/+/sensor/+/data')
print('MQTT subcriber is running.... Waiting for data')

client.loop_forever()
