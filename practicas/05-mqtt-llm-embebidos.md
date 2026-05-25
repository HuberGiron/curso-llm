---
title: "Práctica 5. LLM a MQTT para automatización"
nav_order: 5
parent: "Prácticas tipo FabAcademy"
---
# Práctica 5. LLM a MQTT para automatización

## Objetivo

Conectar un LLM local con MQTT para publicar comandos validados.

## Contexto técnico

MQTT permite desacoplar al LLM del robot, registrar mensajes y probar con un suscriptor simulado.

## Material necesario

- Computadora con Python 3.10 o superior.
- Editor de código.
- Git y repositorio personal.
- Ollama o API indicada según la práctica.
- Dependencias listadas en el código correspondiente.

## Procedimiento sugerido

1. Instala broker local o usa broker de prueba.
2. Ejecuta `codigo/03_llm_mqtt/llm_to_mqtt.py`.
3. Publica tres comandos.
4. Crea suscriptor de prueba.
5. Documenta tópicos.

## Entregables

- [ ] Página de documentación de la práctica.
- [ ] Código fuente en repositorio.
- [ ] Evidencias de ejecución.
- [ ] Tabla de resultados.
- [ ] Análisis de fallas.
- [ ] Conclusión técnica.

## Criterios de evaluación

| Criterio | Excelente | Suficiente | Insuficiente |
|---|---|---|---|
| Reproducibilidad | Cualquier compañero puede repetir la práctica. | Se entiende, pero faltan detalles. | No se puede repetir. |
| Evidencia | Incluye capturas, logs y mediciones. | Incluye evidencia parcial. | No hay evidencia verificable. |
| Análisis | Interpreta resultados y fallas. | Describe resultados sin profundidad. | Sólo muestra que “funcionó”. |
| Código | Claro, ejecutable y comentado. | Funciona con ajustes menores. | Incompleto o no ejecutable. |

## Checklist específico

- [ ] Diagrama de tópicos.
- [ ] Publicador.
- [ ] Suscriptor.
- [ ] Evidencia de mensajes válidos/rechazados.
