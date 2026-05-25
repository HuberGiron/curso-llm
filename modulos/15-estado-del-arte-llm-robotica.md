---
title: "15. Estado del arte: LLM, agentes y robótica"
nav_order: 15
parent: "Módulos académicos"
---
# Estado del arte: LLM, agentes y robótica

## 1. Propósito de esta revisión

Esta página sintetiza el estado del arte que justifica el curso. No es una lista cronológica de modelos; es una lectura crítica sobre cómo la IA generativa se está integrando con sistemas de automatización y robótica, cuáles son las arquitecturas dominantes y qué problemas siguen abiertos.

## 2. Línea conceptual: de lenguaje a acción

El desarrollo de LLM aplicados a robótica puede leerse como una progresión de cuatro etapas:

| Etapa | Capacidad | Ejemplo de pregunta | Riesgo principal |
|---|---|---|---|
| LLM textual | Generar, resumir, clasificar texto | “Explica qué es MQTT” | Respuesta plausible pero no verificada. |
| LLM estructurado | Generar JSON, código o comandos | “Convierte esta orden a JSON” | Formato inválido o parámetros peligrosos. |
| Agente con herramientas | Elegir y llamar funciones | “Consulta estado y decide qué hacer” | Uso incorrecto de herramientas. |
| Modelo encarnado/multimodal | Relacionar percepción, lenguaje y acción | “Toma el objeto rojo” | Grounding físico incompleto. |

Esta progresión muestra por qué el curso no debe quedarse en “usar ChatGPT”. El problema de investigación está en la integración confiable entre modelos probabilísticos y sistemas físicos.

## 3. Transformers y escalamiento

El Transformer introdujo una forma eficiente de modelar dependencias en secuencias mediante atención. Este cambio habilitó modelos de lenguaje entrenados a gran escala. Posteriormente, trabajos sobre escalamiento mostraron relaciones empíricas entre tamaño del modelo, datos y cómputo. Para prospectiva tecnológica, estos trabajos son importantes porque sugieren que el desempeño de modelos no depende únicamente de arquitectura, sino de inversión computacional, disponibilidad de datos y capacidad de despliegue.

**Implicación para robótica:** los laboratorios no siempre necesitan el modelo más grande. Necesitan el modelo más adecuado para una tarea bajo restricciones de latencia, costo y seguridad.

## 4. In-context learning y prompting

GPT-3 popularizó la idea de que un modelo puede adaptarse a tareas mediante instrucciones y ejemplos en el prompt, sin reentrenamiento. En ingeniería, esto convierte al prompt en un artefacto técnico que debe versionarse y evaluarse. En robótica, el prompting se usa para traducir lenguaje natural a intenciones, pero la validación debe vivir fuera del LLM.

Ejemplo de diferencia entre demostración y sistema técnico:

```text
Demo: “El modelo entendió mi instrucción”.
Sistema: “El modelo produjo JSON válido en 97/100 pruebas, con latencia media de 0.8 s, sin violar límites del plano”.
```

## 5. LLM como planeador

Los primeros trabajos de lenguaje como planeación mostraron que un LLM puede proponer pasos de alto nivel. Sin embargo, el conocimiento lingüístico no garantiza que el robot pueda ejecutar esos pasos. Ahí aparece el problema de affordances: una acción debe ser semánticamente correcta y físicamente posible.

SayCan propone una solución híbrida: combinar conocimiento del lenguaje con valores de habilidades disponibles. El LLM responde qué sería razonable hacer; el sistema robótico responde qué puede hacer. Esta idea es fundamental para el curso porque justifica la separación entre agente, skills y validadores.

## 6. ReAct y agentes con herramientas

ReAct propone intercalar razonamiento y acción. En un curso de robótica, esto se traduce en ciclos como:

```text
Objetivo: “lleva el robot al centro y verifica estado”
Pensamiento interno del sistema: necesita moverse y luego consultar estado.
Acción 1: goto(x=0,y=0)
Observación: estado = moving / error = bajo
Acción 2: get_state()
Observación: llegó
Acción 3: stop()
```

No es necesario mostrar razonamiento privado del modelo a los estudiantes; lo importante es registrar acciones, observaciones y resultados. La trazabilidad del agente es un requisito técnico.

## 7. Modelos multimodales y robótica encarnada

PaLM-E y RT-2 representan una línea más avanzada: integrar percepción, lenguaje y acción en modelos multimodales o visión-lenguaje-acción. RT-2, por ejemplo, representa acciones como tokens, lo cual permite reutilizar mecanismos de entrenamiento de modelos lenguaje/visión para acciones robóticas. Esta línea es prometedora, pero no elimina los problemas de seguridad, validación y generalización física.

**Implicación didáctica:** en el curso no se entrena un VLA, pero sí se simula su lógica: imagen o estado → interpretación multimodal → acción estructurada → validación → ejecución.

## 8. Brecha entre investigación y aula/laboratorio

| Investigación avanzada | Implementación viable en curso |
|---|---|
| Entrenar VLA con trayectorias robóticas | Usar VLM comercial para analizar imagen y devolver JSON. |
| Manipulador móvil real con affordances | Robot virtual o ESP32 con acciones discretas. |
| Modelo multimodal de cientos de miles de millones de parámetros | Modelo local pequeño + comparación con API. |
| Evaluación con miles de episodios | Benchmark académico con 20–100 prompts controlados. |

## 9. Preguntas abiertas para discusión

1. ¿Cuándo un LLM es interfaz y cuándo empieza a ser controlador?
2. ¿Qué tareas robóticas deberían prohibirse a un LLM?
3. ¿Qué nivel de latencia es aceptable para un robot móvil educativo?
4. ¿Qué significa “seguridad” en un prototipo académico?
5. ¿Cómo se documenta una falla de un agente de forma útil para investigación?

## 10. Fuentes principales

- Vaswani, A. et al. (2017). *Attention Is All You Need*. <https://arxiv.org/abs/1706.03762>
- Brown, T. B. et al. (2020). *Language Models are Few-Shot Learners*. <https://arxiv.org/abs/2005.14165>
- Kaplan, J. et al. (2020). *Scaling Laws for Neural Language Models*. <https://arxiv.org/abs/2001.08361>
- Ahn, M. et al. (2022). *Do As I Can, Not As I Say*. <https://arxiv.org/abs/2204.01691>
- Yao, S. et al. (2022). *ReAct*. <https://arxiv.org/abs/2210.03629>
- Driess, D. et al. (2023). *PaLM-E*. <https://arxiv.org/abs/2303.03378>
- Zitkovich, B. et al. (2023). *RT-2*. <https://arxiv.org/abs/2307.15818>
