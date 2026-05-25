---
title: "8. MQTT, WebSocket y comunicación eficiente"
nav_order: 8
parent: "Módulos académicos"
---
# MQTT, WebSocket y comunicación eficiente

## 1. Problema de comunicación

Un sistema LLM-robot no termina cuando el modelo genera texto. Es necesario transportar comandos, estados y mediciones entre componentes. Para prototipos web y robóticos usaremos dos tecnologías:

- **MQTT:** comunicación publish/subscribe ligera para IoT.
- **WebSocket:** canal bidireccional persistente entre navegador y servidor.

## 2. MQTT

MQTT usa un broker. Los clientes no se comunican directamente entre sí; publican y se suscriben a tópicos.

```text
LLM backend → publish → huber/robot/cmd
Robot/simulador → subscribe → huber/robot/cmd
Robot/simulador → publish → huber/robot/state
Dashboard → subscribe → huber/robot/state
```

La especificación MQTT 5.0 lo define como un protocolo cliente-servidor publish/subscribe, ligero y adecuado para entornos M2M e IoT.

## 3. WebSocket

WebSocket mantiene una conexión abierta entre navegador y servidor. Es útil cuando se requiere interacción en tiempo real sin polling HTTP.

```javascript
const ws = new WebSocket("ws://localhost:8000/ws");
ws.onmessage = (event) => console.log(event.data);
ws.send(JSON.stringify({cmd:"ping"}));
```

## 4. Comparación

| Criterio | MQTT | WebSocket |
|---|---|---|
| Patrón | Publish/subscribe | Cliente-servidor bidireccional |
| Ideal para | IoT, sensores, robots | Interfaces web en tiempo real |
| Intermediario | Broker | Servidor WebSocket |
| Tópicos | Sí | No nativo |
| Navegador | Requiere MQTT sobre WebSocket | Nativo |

## 5. Diseño de tópicos para curso

```text
curso/robot/cmd
curso/robot/state
curso/robot/log
curso/robot/plan/status
curso/robot/safety
```

Reglas:

- No generar tópicos dinámicos desde el LLM.
- No mezclar comandos y telemetría.
- Registrar timestamp.
- Mantener payloads JSON pequeños.
- Validar cualquier mensaje antes de ejecutarlo.

## 6. Ejercicio

Crear un publicador y un suscriptor. El publicador manda comandos `goto`, `stop`, `circle`. El suscriptor imprime, valida y rechaza comandos inválidos.

{: .evidencia }
> Captura de broker funcionando, script publicador, script suscriptor y tabla con tres mensajes válidos y tres inválidos.

## 7. Fuentes

- OASIS MQTT 5.0. <https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html>
- MQTT.org specification. <https://mqtt.org/mqtt-specification/>
- MDN WebSocket API. <https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API>
