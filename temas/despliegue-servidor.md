---
layout: default
title: "07 Despliegue local/remoto y documentación reproducible"
parent: "Temas"
nav_order: 7
---
# 07 Despliegue local/remoto y documentación reproducible

<div class="callout"><strong>Objetivo:</strong> Preparar un backend ejecutable localmente o en servidor, cuidando CORS, HTTPS, variables de entorno y documentación.</div>


## Ideas centrales para la clase

Un prototipo académico debe ser reproducible. No basta con que funcione en la computadora de un equipo: debe explicar cómo instalar dependencias, configurar variables, ejecutar backend, abrir frontend y probar endpoints.

En servidores web se revisan: CORS, HTTPS, Nginx o proxy inverso, logs, manejo de errores y separación entre frontend estático y backend dinámico.

## Checklist de despliegue

- `requirements.txt` o `environment.yml`.
- `.env.example` sin secretos reales.
- Comando de ejecución local.
- Endpoint `/health` o prueba mínima.
- Captura de Swagger/OpenAPI si se usa FastAPI.
- Tabla de errores frecuentes.


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
- [dotenv](https://pypi.org/project/python-dotenv/)
- [justdocs](https://just-the-docs.com/)
