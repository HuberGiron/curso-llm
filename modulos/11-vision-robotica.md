---
title: "11. Modelos visión-lenguaje y robótica"
nav_order: 11
parent: "Módulos académicos"
---
# Modelos visión-lenguaje y robótica

## 1. De LLM a VLM/VLA

Un LLM tradicional opera sobre texto. Un modelo visión-lenguaje (VLM) integra imágenes y texto. Un modelo visión-lenguaje-acción (VLA) busca relacionar percepción visual, lenguaje y acciones robóticas.

En robótica, el problema principal es el **grounding**: conectar palabras con estados físicos, objetos, affordances y límites reales.

## 2. Ejemplos de literatura reciente

### SayCan

SayCan combina conocimiento lingüístico de modelos grandes con funciones de valor asociadas a habilidades robóticas. La idea es: el LLM puede proponer pasos plausibles, pero el robot debe elegir acciones que puede ejecutar en su entorno.

### PaLM-E

PaLM-E propone incorporar modalidades continuas, visuales y de estado robótico dentro de un modelo multimodal para tareas de razonamiento encarnado.

### RT-2

RT-2 representa acciones robóticas como tokens, integrando datos web visión-lenguaje con datos de trayectorias robóticas. Esto ilustra una dirección prospectiva importante: modelos que no sólo describen acciones, sino que producen políticas o acciones discretizadas.

## 3. Aplicación didáctica viable

En un curso de 6 semanas, no entrenaremos un VLA. Sí podemos construir un prototipo donde:

1. Una cámara captura imagen.
2. Un modelo multimodal describe escena.
3. Un agente decide una acción de alto nivel.
4. Un validador convierte la acción a comando.
5. Un robot virtual o físico ejecuta.

## 4. Ejemplo de prompt visual

```text
Observa la imagen del área de trabajo. Identifica si hay un obstáculo frente al robot.
Responde sólo JSON:
{"obstacle": true|false, "relative_position":"front|left|right|none", "confidence":0-1}
```

## 5. Limitaciones

- Los VLM pueden interpretar mal distancias.
- Una imagen 2D no garantiza geometría 3D confiable.
- La latencia suele ser mayor que en texto.
- El modelo puede confundir objetos no vistos.
- Se requiere calibración y validación externa.

## 6. Ejercicio

Tomar tres imágenes de un entorno de robot y pedir a un modelo multimodal que identifique obstáculos. Comparar contra una etiqueta humana.

{: .evidencia }
> Reporte con imágenes, prompt, respuesta JSON, clasificación humana y matriz simple de acierto/error.

## 7. Fuentes

- Ahn et al. *Do As I Can, Not As I Say*. <https://arxiv.org/abs/2204.01691>
- Driess et al. *PaLM-E*. <https://arxiv.org/abs/2303.03378>
- Zitkovich et al. *RT-2*. <https://arxiv.org/abs/2307.15818>
