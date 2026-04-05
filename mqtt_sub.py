import os
import sys
import json
import paho.mqtt.client as mqtt
from django import setup

# 1. Path Setup
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 2. Django Setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings') 
setup()

from data.models import Data
from sensors.models import Sensors
from debug.models import DebugLog
from devices.models import Devices

# --- HiveMQ Credentials (Wahi jo D1 Mini me dale hain) ---
MQTT_BROKER = "5ed07714471b4d5cb60646954c0c4361.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USER = "freeUser1" # HiveMQ Dashboard se lo
MQTT_PASS = "freeUser1"

def on_message(client, userdata, msg):
    msg_payload = None
    topic_to_insert = msg.topic
    try:
        topic_parts = msg.topic.split('/')
        device_id_in_topic = topic_parts[2]
        sens_id_in_topic = topic_parts[4]
        
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
            print(f'Saved: {value_to_insert} for Sensor ID: {sens_id_in_topic}', flush=True)
        else:
            print(f'Sensor ID {sens_id_in_topic} not found.', flush=True)

    except Exception as err:
        print(f"Callback Error: {err}", flush=True)

# 3. MQTT Client Setup
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# TLS Settings (HiveMQ Cloud ke liye zaroori hai)
client.tls_set() 

# Authentication
client.username_pw_set(MQTT_USER, MQTT_PASS)

client.on_message = on_message

print(f'Connecting to {MQTT_BROKER}...')
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe('edgef/device/+/sensor/+/data')

print('MQTT Subscriber is running... (Waiting for messages)')
client.loop_forever()
