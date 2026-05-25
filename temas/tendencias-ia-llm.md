---
layout: default
title: "01 Tendencias, IA generativa y LLM"
parent: "Temas"
nav_order: 1
---
# 01 Tendencias, IA generativa y LLM

<div class="callout"><strong>Objetivo:</strong> Comprender la relación entre prospectiva tecnológica, IA generativa, Transformers, modelos LLM, modelos open source/comerciales, Hugging Face y Ollama.</div>


## Ideas centrales para la clase

La prospectiva tecnológica no se limita a adivinar el futuro. En este curso se usa como una metodología para observar señales, comparar trayectorias tecnológicas y tomar decisiones sobre qué tecnología conviene adoptar, prototipar o descartar.

En IA generativa, el punto de quiebre técnico que explica gran parte del avance reciente es la arquitectura **Transformer**. El artículo *Attention Is All You Need* propone una arquitectura basada en mecanismos de atención, sin recurrencia ni convoluciones como componentes centrales. Para el curso no es necesario derivar toda la matemática, pero sí entender que esta arquitectura permite procesar secuencias de texto de forma paralelizable y escalable.

Un LLM puede analizarse desde cinco dimensiones: arquitectura, número de parámetros, tamaño de contexto, tokenizer, datos de entrenamiento y alineación/instrucción. Para seleccionar un modelo en robótica no basta con preguntar cuál es “mejor”; se debe evaluar latencia, idioma, precisión de salida estructurada, consumo de memoria, licencia y facilidad de despliegue.

## Actividad guiada

El profesor muestra cómo comparar modelos en Hugging Face y Ollama. Los estudiantes identifican modelo, licencia, tamaño, cuantización, idioma dominante, modalidad y requerimientos estimados.

## Producto de la sesión

Mapa de tendencias: IA generativa, LLM locales, APIs comerciales, agentes, visión-lenguaje-acción y automatización.


## Checklist mínimo de evidencia

- [ ] Conceptos principales explicados con tus propias palabras.
- [ ] Diagrama o tabla técnica del tema.
- [ ] Evidencia de demo, práctica o prueba.
- [ ] Resultado medible cuando aplique: latencia, costo, tokens, éxito/falla o errores.
- [ ] Reflexión: ¿qué implicación tiene esto para automatización o robótica?
- [ ] Fuentes consultadas y citadas.

## Fuentes citadas

- [transformer](https://arxiv.org/abs/1706.03762)
- [hf_transformers](https://huggingface.co/docs/transformers/en/index)
- [ollama_api](https://docs.ollama.com/api/introduction)
