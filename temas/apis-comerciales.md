---
layout: default
title: "06 APIs comerciales: Gemini, Claude, Grok, OpenAI y secretos"
parent: "Temas"
nav_order: 6
---
# 06 APIs comerciales: Gemini, Claude, Grok, OpenAI y secretos

<div class="callout"><strong>Objetivo:</strong> Comparar APIs comerciales frente a modelos locales y manejar llaves, costos, cuotas y riesgos.</div>


## Ideas centrales para la clase

Las APIs comerciales ofrecen modelos de alta capacidad sin administrar infraestructura local, pero introducen costo por uso, dependencia de proveedor, límites de cuota, requisitos de conectividad y riesgos de exposición de llaves.

Nunca se deben subir llaves API a GitHub. Las llaves deben guardarse en variables de entorno, archivos `.env` excluidos por `.gitignore` o gestores de secretos del servidor.

## Matriz de comparación

| Criterio | Modelo local | API comercial |
|---|---|---|
| Costo marginal | Energía/hardware | Tokens/solicitudes |
| Privacidad | Mayor control local | Depende del proveedor |
| Latencia | Depende del equipo | Depende de red/proveedor |
| Calidad | Depende del modelo instalado | Usualmente alta en modelos frontera |
| Riesgo | mantenimiento local | dependencia externa |

## Actividad

Construir una matriz actualizada con precios oficiales consultados el día de la práctica.


## Checklist mínimo de evidencia

- [ ] Conceptos principales explicados con tus propias palabras.
- [ ] Diagrama o tabla técnica del tema.
- [ ] Evidencia de demo, práctica o prueba.
- [ ] Resultado medible cuando aplique: latencia, costo, tokens, éxito/falla o errores.
- [ ] Reflexión: ¿qué implicación tiene esto para automatización o robótica?
- [ ] Fuentes consultadas y citadas.

## Fuentes citadas

- [gemini_api](https://ai.google.dev/gemini-api/docs)
- [gemini_pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [anthropic_docs](https://platform.claude.com/docs/en/home)
- [anthropic_pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [xai_docs](https://docs.x.ai/overview)
- [xai_models](https://docs.x.ai/developers/models)
- [openai_models](https://developers.openai.com/api/docs/models)
- [openai_pricing](https://openai.com/api/pricing/)
- [dotenv](https://pypi.org/project/python-dotenv/)
