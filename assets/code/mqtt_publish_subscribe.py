"""Publicador/suscriptor MQTT mínimo para prácticas.
Instalar: pip install paho-mqtt
"""
import json, time, paho.mqtt.client as mqtt

HOST = 'test.mosquitto.org'
PORT = 1883
TOPIC = 'huber/robot/plan/cmd'

def on_connect(client, userdata, flags, rc, properties=None):
    print('Conectado rc=', rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print('Mensaje recibido:', msg.topic, msg.payload.decode(errors='ignore'))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(HOST, PORT, keepalive=60)
client.loop_start()

for i in range(3):
    payload = {'cmd': 'PING', 'trial': i + 1, 't': time.time()}
    client.publish(TOPIC, json.dumps(payload), qos=0, retain=False)
    time.sleep(1)

client.loop_stop()
client.disconnect()
