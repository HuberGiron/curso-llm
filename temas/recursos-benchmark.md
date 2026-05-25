---
layout: default
title: "02 Recursos de cómputo, costos y benchmark"
parent: "Temas"
nav_order: 2
---
# 02 Recursos de cómputo, costos y benchmark

<div class="callout"><strong>Objetivo:</strong> Medir recursos, latencia y costos asociados al uso de LLM en CPU, GPU, nube y entornos embebidos.</div>


## Ideas centrales para la clase

Un LLM no se evalúa únicamente por la calidad de sus respuestas. En automatización y robótica importan la latencia, la estabilidad, el costo por ejecución, la disponibilidad y el control sobre la infraestructura.

Para modelos locales se revisan: CPU, GPU, RAM, VRAM, cuantización, tamaño del modelo y número máximo de tokens. Para APIs comerciales se revisan: costo por tokens de entrada/salida, límites de uso, privacidad, disponibilidad, dependencia del proveedor y manejo de secretos.

## Metodología de benchmark

1. Fijar un prompt de prueba.
2. Ejecutar N repeticiones por modelo.
3. Registrar tiempo total, tokens de entrada, tokens de salida y errores.
4. Calcular promedio, desviación, máximo y mínimo.
5. Comparar calidad de salida con una rúbrica sencilla.

## Demo sugerida

Usar `assets/code/benchmark_ollama.py` para medir un modelo local y guardar CSV.


## Checklist mínimo de evidencia

- [ ] Conceptos principales explicados con tus propias palabras.
- [ ] Diagrama o tabla técnica del tema.
- [ ] Evidencia de demo, práctica o prueba.
- [ ] Resultado medible cuando aplique: latencia, costo, tokens, éxito/falla o errores.
- [ ] Reflexión: ¿qué implicación tiene esto para automatización o robótica?
- [ ] Fuentes consultadas y citadas.

## Fuentes citadas

- [ollama_api](https://docs.ollama.com/api/introduction)
- [hf_generation](https://huggingface.co/docs/transformers/en/main_classes/text_generation)
- [openai_pricing](https://openai.com/api/pricing/)
- [gemini_pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [anthropic_pricing](https://platform.claude.com/docs/en/about-claude/pricing)
