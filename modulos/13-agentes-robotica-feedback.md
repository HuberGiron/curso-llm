---
title: "13. Agentes LLM como planeadores con retroalimentación"
nav_order: 13
parent: "Módulos académicos"
---
# Agentes LLM como planeadores con retroalimentación

## 1. Planeación de alto nivel vs control

Un agente LLM puede actuar como planeador de alto nivel, pero el control de bajo nivel debe permanecer en módulos deterministas. Esta separación evita que una respuesta probabilística gobierne directamente motores o actuadores.

```text
Agente: decide "hacer círculo".
Planner: genera puntos de referencia.
Controlador: calcula velocidades.
Robot: ejecuta.
Sensor: reporta estado.
Agente: ajusta objetivo o solicita recuperación.
```

## 2. Retroalimentación

La retroalimentación puede incluir:

- Pose estimada.
- Estado de conexión.
- Error de seguimiento.
- Obstáculos.
- Confirmación de ejecución.
- Mensajes de falla.

El agente sólo debe recibir información relevante y resumida. Enviar demasiada telemetría al prompt aumenta costo y puede degradar decisiones.

## 3. Ejemplo de estado compacto

```json
{
  "robot_id": "R1",
  "pose": {"x": 12.4, "y": 88.1, "theta": 1.57},
  "goal": {"x": 0, "y": 100},
  "tracking_error": 14.2,
  "battery": 0.82,
  "last_cmd_ok": true
}
```

## 4. Patrón seguro de decisión

1. El agente propone acción.
2. El sistema simula o valida.
3. El usuario o política autoriza si es crítico.
4. El planner ejecuta.
5. El sistema observa.
6. Si falla, el agente propone recuperación.

## 5. Métricas de proyecto

- % instrucciones interpretadas correctamente.
- % comandos rechazados por seguridad.
- Latencia promedio de decisión.
- Error de seguimiento.
- Número de reintentos.
- Calidad de documentación.

## 6. Actividad

Diseñar el ciclo de retroalimentación del proyecto final. Definir qué datos entran al prompt y cuáles se quedan fuera.

{: .evidencia }
> Diagrama del ciclo, schema del estado, política de rechazo y lista de métricas.

## 7. Fuentes

- Ahn et al. *SayCan*. <https://arxiv.org/abs/2204.01691>
- Yao et al. *ReAct*. <https://arxiv.org/abs/2210.03629>
- NIST AI RMF. <https://www.nist.gov/itl/ai-risk-management-framework>
