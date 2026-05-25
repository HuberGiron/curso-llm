---
title: "7. Prompting, configuración y salida estructurada"
nav_order: 7
parent: "Módulos académicos"
---
# Prompting, configuración y salida estructurada

## 1. Prompting como ingeniería de interfaz

El prompting no debe entenderse como “frases mágicas”. En sistemas técnicos, un prompt es una interfaz entre un usuario humano y un sistema computacional probabilístico. Debe especificar rol, contexto, formato, restricciones y criterio de rechazo.

## 2. Anatomía de un prompt robusto

```text
ROL: Eres un intérprete de instrucciones para un robot móvil.
CONTEXTO: El plano mide x=[-500,500], y=[-300,300].
TAREA: Convierte instrucciones en JSON.
FORMATO: {"intent":"goto|circle|stop", ...}
RESTRICCIONES: No inventes campos. Si falta información, usa defaults.
SALIDA: Sólo JSON válido. No markdown. No explicación.
EJEMPLOS: ...
INSTRUCCIÓN: ...
```

## 3. Temperatura y reproducibilidad

Para control de robots se recomienda temperatura baja. Una temperatura alta puede ser útil en lluvia de ideas o generación creativa, pero perjudica consistencia de formato.

| Uso | Temperatura sugerida |
|---|---:|
| JSON para robot | 0.0–0.2 |
| Clasificación | 0.0–0.3 |
| Explicación académica | 0.3–0.6 |
| Ideación | 0.7–1.0 |

## 4. Diseño de schema para robot

Ejemplo de schema simple:

```json
{
  "intent": "goto",
  "x": 0,
  "y": 0,
  "duration_s": 5,
  "speed": null,
  "safety": {
    "stop_if_obstacle": true,
    "max_speed": 0.3
  }
}
```

## 5. Validación programática

El prompt reduce errores; el validador los controla.

```python
from pydantic import BaseModel, Field
from typing import Literal, Optional

class RobotCommand(BaseModel):
    intent: Literal["goto", "circle", "stop"]
    x: Optional[float] = Field(default=None, ge=-500, le=500)
    y: Optional[float] = Field(default=None, ge=-300, le=300)
    duration_s: Optional[float] = Field(default=5, gt=0, le=120)
```

## 6. Antipatrones

- Pedir “hazlo bien” sin especificar formato.
- Mezclar conversación abierta con comandos críticos.
- Permitir que el LLM invente tópicos MQTT o pines.
- Confiar en una sola respuesta sin validación.
- Usar prompts demasiado largos que no se actualizan ni se prueban.

## 7. Ejercicio

Diseñar tres versiones de prompt para el mismo robot y medir:

- JSON válido.
- Interpretación correcta.
- Longitud de prompt.
- Latencia.

{: .evidencia }
> Reporte con comparación de prompts, ejemplos de falla y propuesta final.

## 8. Fuentes

- Hugging Face text generation parameters. <https://huggingface.co/docs/transformers/en/main_classes/text_generation>
- OpenAI structured outputs/function calling docs. <https://developers.openai.com/api/reference/overview/>
- Gemini function calling docs. <https://ai.google.dev/gemini-api/docs/function-calling>
