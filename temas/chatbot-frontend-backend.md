---
layout: default
title: "03 LLM como chatbot: frontend y backend"
parent: "Temas"
nav_order: 3
---
# 03 LLM como chatbot: frontend y backend

<div class="callout"><strong>Objetivo:</strong> Construir una interfaz básica donde un frontend web se comunica con un backend Python y este llama a un LLM local.</div>


## Ideas centrales para la clase

Un chatbot académico mínimo tiene tres capas: frontend, backend y modelo. El frontend captura el prompt, el backend valida parámetros, llama al modelo y registra métricas. El modelo no debe quedar conectado directamente a la interfaz sin control, porque se pierde trazabilidad y validación.

Se recomienda FastAPI cuando se quiere documentación automática, validación con tipos y endpoints claros. Flask es suficiente para aplicaciones pequeñas, pero FastAPI facilita prácticas con esquemas y documentación interactiva.

## Arquitectura

![Arquitectura LLM local](../assets/img/diagramas/arquitectura-llm-local.svg)

## Demo sugerida

- Backend: `assets/code/chatbot_backend_fastapi.py`
- Frontend: `assets/code/frontend_chatbot.html`


## Checklist mínimo de evidencia

- [ ] Conceptos principales explicados con tus propias palabras.
- [ ] Diagrama o tabla técnica del tema.
- [ ] Evidencia de demo, práctica o prueba.
- [ ] Resultado medible cuando aplique: latencia, costo, tokens, éxito/falla o errores.
- [ ] Reflexión: ¿qué implicación tiene esto para automatización o robótica?
- [ ] Fuentes consultadas y citadas.

## Fuentes citadas

- [fastapi](https://fastapi.tiangolo.com/)
- [fastapi_docs](https://fastapi.tiangolo.com/reference/openapi/docs/)
- [ollama_api](https://docs.ollama.com/api/introduction)
- [flask](https://flask.palletsprojects.com/en/stable/quickstart/)
