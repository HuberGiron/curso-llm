---
layout: default
title: "04 Prompting, selección de modelo y salida estructurada"
parent: "Temas"
nav_order: 4
---
# 04 Prompting, selección de modelo y salida estructurada

<div class="callout"><strong>Objetivo:</strong> Diseñar prompts robustos para transformar lenguaje natural en instrucciones verificables, especialmente JSON para sistemas robóticos.</div>


## Ideas centrales para la clase

Un buen prompt para robótica debe reducir ambigüedad y forzar estructura. En lugar de pedir “controla el robot”, se define rol, contexto, rango de operación, formato de salida, ejemplos, restricciones y condición de falla segura.

La salida estructurada es esencial. Cuando un LLM controla o asiste un sistema físico, el texto libre debe convertirse en un objeto validable por software. El patrón mínimo es: instrucción humana → prompt → JSON → validación → acción.

## Plantilla base de prompt

```text
Rol: eres un traductor de instrucciones humanas a comandos robóticos.
Contexto: el robot opera en un plano x,y limitado.
Tarea: devuelve un JSON con intención y parámetros.
Restricción: si la instrucción es ambigua, responde con stop.
Formato: SOLO JSON válido.
```

## Ejercicio

Probar 10 instrucciones ambiguas y comparar: salida esperada, salida obtenida, falla y corrección del prompt.


## Checklist mínimo de evidencia

- [ ] Conceptos principales explicados con tus propias palabras.
- [ ] Diagrama o tabla técnica del tema.
- [ ] Evidencia de demo, práctica o prueba.
- [ ] Resultado medible cuando aplique: latencia, costo, tokens, éxito/falla o errores.
- [ ] Reflexión: ¿qué implicación tiene esto para automatización o robótica?
- [ ] Fuentes consultadas y citadas.

## Fuentes citadas

- [hf_generation](https://huggingface.co/docs/transformers/en/main_classes/text_generation)
- [openai_structured](https://developers.openai.com/api/docs/guides/structured-outputs)
- [openai_functions](https://developers.openai.com/api/docs/guides/function-calling)
