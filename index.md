---
title: "Inicio"
nav_order: 1
---
# Prospectiva Tecnológica: IA con LLM para Automatización y Robótica

<div class="lead">
Este sitio funciona como manual académico, guía de clase, repositorio de prácticas y base documental para un curso intensivo de prospectiva tecnológica enfocado en inteligencia artificial generativa, modelos de lenguaje, agentes y automatización robótica.
</div>

{: .objetivo }
> El objetivo no es únicamente aprender a “usar chatbots”, sino comprender cómo se construyen sistemas donde un LLM interpreta instrucciones humanas, razona sobre una tarea, genera comandos estructurados, se comunica con software/hardware y se evalúa con métricas técnicas, económicas y de seguridad.

## Cómo está organizado

<div class="grid-2">
<div class="course-card">
<h3>1. Fundamentos y estado del arte</h3>
<p>IA generativa, Transformers, modelos abiertos/comerciales, tokens, parámetros, memoria, GPU/CPU, inferencia y tendencias tecnológicas.</p>
</div>
<div class="course-card">
<h3>2. Implementación técnica</h3>
<p>Ollama, Python, FastAPI, HTML/CSS/JS, APIs locales, MQTT, WebSocket, secretos, servidores y despliegue.</p>
</div>
<div class="course-card">
<h3>3. Robótica y automatización</h3>
<p>LLM como interfaz, LLM como planeador, agentes con skills, retroalimentación por sensores, visión-lenguaje y seguridad operacional.</p>
</div>
<div class="course-card">
<h3>4. Prácticas tipo FabAcademy</h3>
<p>Cada práctica exige repositorio, evidencia, código, pruebas, mediciones, reflexión técnica y checklist de entregables.</p>
</div>
</div>

## Ruta sugerida para clase

1. Leer el módulo antes de clase.
2. Seguir la explicación del profesor usando la página como material base.
3. Ejecutar el código mínimo en clase.
4. Documentar el proceso en un repositorio personal tipo FabAcademy.
5. Cerrar cada práctica con evidencias, mediciones y reflexión crítica.

## Arquitectura guía del curso

![Arquitectura LLM Robotica](assets/diagrams/arquitectura_llm_robotica.svg){: .diagram }

## Principio de trabajo

En un sistema robótico, el LLM debe trabajar como una capa de interpretación, planeación o coordinación. No debe sustituir directamente a los controladores de bajo nivel ni enviar señales inseguras a actuadores. El flujo recomendado es:

```text
Lenguaje natural → LLM/agente → JSON validado → planner/reglas → comunicación → robot/simulador → sensores → retroalimentación
```

## Entregables permanentes del curso

- Repositorio individual con bitácora técnica por práctica.
- Código ejecutable y documentado.
- Capturas, gráficas, videos o evidencias reproducibles.
- Análisis de fallas, limitaciones y decisiones de diseño.
- Proyecto final con prototipo funcional y evaluación.
