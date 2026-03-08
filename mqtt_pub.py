import paho.mqtt.client as mqtt
import random
import json
import time

# Emqx details:
broker = 'localhost'
port = 1883

client_id = 'Sensor_Simulator'

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id)
client.connect(broker, port)

# value in payload,

device_id = 5
sensor_id = 9

def generate_and_post():

    sens_value = round(random.uniform(-100, 2100), 2)

    payload = {
        'value': sens_value,
    }
    
    topic = f'edgef/device/{device_id}/sensor/{sensor_id}/data'
    
    client.publish(topic, json.dumps(payload)) 
    
    print(f'Published Value: {payload["value"]}, to sensor: {sensor_id}')
    
    time.sleep(1)


while True:
    generate_and_post()