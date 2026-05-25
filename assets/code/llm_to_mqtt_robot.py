"""Ejemplo educativo: LLM local interpreta una instrucción y publica JSON por MQTT.
No usar en un robot físico sin validadores, paro seguro y supervisión humana.
"""
import json, os, requests, paho.mqtt.client as mqtt

OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
MODEL = os.getenv('OLLAMA_MODEL', 'llama3.1:8b')
MQTT_HOST = os.getenv('MQTT_HOST', 'test.mosquitto.org')
MQTT_TOPIC = os.getenv('MQTT_TOPIC', 'huber/robot/plan/cmd')

SYSTEM = """Devuelve SOLO JSON válido para controlar un robot virtual.
Esquema: {"intent":"goto|stop|circle", "x":number, "y":number, "radius":number, "duration_s":number}
Si la instrucción es ambigua o insegura usa {"intent":"stop"}."""

def interpret(instruction: str) -> dict:
    prompt = SYSTEM + '\nInstrucción: ' + instruction
    r = requests.post(f'{OLLAMA_BASE_URL}/api/generate', json={
        'model': MODEL, 'prompt': prompt, 'stream': False,
        'options': {'temperature': 0.0, 'num_predict': 160}
    }, timeout=120)
    r.raise_for_status()
    text = r.json().get('response', '').strip()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = {'intent': 'stop'}
    return validate(data)

def validate(cmd: dict) -> dict:
    allowed = {'goto', 'stop', 'circle'}
    if cmd.get('intent') not in allowed:
        return {'intent': 'stop'}
    for k in ['x','y','radius','duration_s']:
        if k in cmd:
            try:
                cmd[k] = float(cmd[k])
            except Exception:
                cmd[k] = 0.0
    return cmd

if __name__ == '__main__':
    instruction = input('Instrucción: ')
    cmd = interpret(instruction)
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(MQTT_HOST, 1883, 60)
    client.publish(MQTT_TOPIC, json.dumps(cmd), qos=0, retain=False)
    client.disconnect()
    print('Publicado:', cmd)
