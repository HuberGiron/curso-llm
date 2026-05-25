---
title: "3. LLM a MQTT y robot virtual"
nav_order: 3
parent: "Instructivos paso a paso"
---
# LLM a MQTT y robot virtual

## 1. Objetivo

Conectar la salida validada de un LLM con un canal MQTT para que otro programa pueda recibir comandos de robot.

## 2. Arquitectura

```text
Usuario → Python LLM client → Validador → MQTT broker → Robot virtual/suscriptor
```

## 3. Tópicos sugeridos

```text
curso/robot/cmd      comandos aceptados
curso/robot/state    estado del robot
curso/robot/log      eventos del sistema
curso/robot/safety   rechazos o alertas
```

## 4. Publicador

El archivo base está en:

```text
codigo/03_llm_mqtt/llm_to_mqtt.py
```

Ejecutar:

```bash
cd codigo/03_llm_mqtt
pip install -r requirements.txt
python llm_to_mqtt.py
```

## 5. Suscriptor de prueba

```python
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("curso/robot/#")
client.loop_forever()
```

## 6. Pruebas de aceptación

| Prueba | Esperado |
|---|---|
| “Ve al centro” | Publica `goto`. |
| “Detente” | Publica `stop`. |
| “Ve a 9999,9999” | Rechaza. |
| “Activa un motor a máxima potencia” | Rechaza si no existe skill. |

## 7. Evidencia recomendada

- Captura del publicador.
- Captura del suscriptor.
- Mensajes JSON.
- Video corto del flujo.
- Diagrama de tópicos.

## 8. Checklist

- [ ] Broker probado.
- [ ] Publicador funcionando.
- [ ] Suscriptor funcionando.
- [ ] Comandos válidos publicados.
- [ ] Comandos inválidos rechazados.
- [ ] Explicación de seguridad.
