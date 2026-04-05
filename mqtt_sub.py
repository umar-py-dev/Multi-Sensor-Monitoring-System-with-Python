import os
import sys
import json
import paho.mqtt.client as mqtt
from django import setup

# 1. Path Setup: Current directory ko path mein add karein
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 2. Django Settings Module (Apne project folder ka sahi naam check kar lein)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings') 
setup()

# Models Import (setup() ke baad hi honge)
from data.models import Data
from sensors.models import Sensors
from debug.models import DebugLog
from devices.models import Devices

def on_message(client, userdata, msg):
    msg_payload = None
    topic_to_insert = msg.topic # Default in case of error
    try:
        topic_parts = msg.topic.split('/')
        device_id_in_topic = topic_parts[2]
        sens_id_in_topic = topic_parts[4]
        
        # Device information fetch karein
        device_object = Devices.objects.filter(id=device_id_in_topic).first()
        if device_object:
            devic_type = device_object.device_type_id
            topic_parts[2] = str(devic_type)
            topic_to_insert = '/'.join(topic_parts)
        
        msg_payload = json.loads(msg.payload.decode())
        value_to_insert = msg_payload.get('value')
        
        sensor_obj = Sensors.objects.filter(id=sens_id_in_topic).first()
        
        if sensor_obj:
            Data.objects.create(sensor_id=sensor_obj, value=value_to_insert)
            DebugLog.objects.create(
                payload=msg_payload,
                topic=topic_to_insert,
                response='Data Inserted Successfully'
            )
            print(f'Saved: {value_to_insert} for Sensor ID: {sens_id_in_topic}')
        else:
            print(f'Sensor ID {sens_id_in_topic} not found.')

    except Exception as err:
        DebugLog.objects.create(
            topic=topic_to_insert,
            payload=msg_payload if msg_payload else {},
            response=str(err)
        )
        print(f"Error: {err}")


MQTT_BROKER = "5ed07714471b4d5cb60646954c0c4361.s1.eu.hivemq.cloud" # HiveMQ free for testing
MQTT_PORT = 8883

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

# Connection
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe('edgef/device/+/sensor/+/data')

print(f'MQTT Subscriber running on {MQTT_BROKER}... Waiting for data')
client.loop_forever()
