---
title: "9. LLM para controlar sistemas embebidos"
nav_order: 9
parent: "Módulos académicos"
---
# LLM para controlar sistemas embebidos

## 1. Idea central

Un LLM puede ser una interfaz de alto nivel para sistemas embebidos, pero no debe operar como controlador de bajo nivel. La arquitectura recomendada separa:

- Interpretación semántica.
- Validación.
- Planeación.
- Comunicación.
- Control embebido.
- Seguridad.

## 2. Ejemplo: LED o actuador simple

Instrucción humana:

```text
Parpadea el LED tres veces cada 200 ms.
```

JSON esperado:

```json
{"device":"led","action":"blink","times":3,"period_ms":200}
```

El microcontrolador no recibe texto libre. Recibe un comando validado.

## 3. Ejemplo: robot móvil virtual

Instrucción:

```text
Traza un círculo de radio 100 centrado en (10,300), una vuelta en 60 segundos.
```

JSON esperado:

```json
{
  "intent": "circle",
  "center": {"x": 10, "y": 300},
  "radius": 100,
  "turns": 1,
  "duration_s": 60
}
```

El planner transforma ese JSON en una secuencia de referencias temporales.

## 4. Capa de seguridad

Antes de publicar por MQTT:

1. Validar JSON.
2. Verificar rango de coordenadas.
3. Verificar velocidad máxima.
4. Rechazar acciones desconocidas.
5. Registrar el comando.
6. Permitir paro manual.

## 5. Código base

Ver:

```text
codigo/03_llm_mqtt/llm_to_mqtt.py
```

## 6. Práctica en clase

Conectar un LLM local con MQTT para publicar comandos de alto nivel. Un suscriptor simulado debe imprimir comandos aceptados/rechazados.

{: .evidencia }
> Entregar video corto del flujo completo, código, diagrama de tópicos y análisis de fallas.

## 7. Fuentes

- MQTT 5.0 OASIS. <https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html>
- Ollama API. <https://docs.ollama.com/api/introduction>
- Ahn et al. *Do As I Can, Not As I Say*. <https://arxiv.org/abs/2204.01691>
