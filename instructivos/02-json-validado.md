---
title: "2. De lenguaje natural a JSON validado"
nav_order: 2
parent: "Instructivos paso a paso"
---
# De lenguaje natural a JSON validado

## 1. Objetivo

Construir un flujo donde el LLM recibe lenguaje natural y produce un comando JSON que será validado antes de usarse.

## 2. Definir espacio de trabajo

Para el curso usaremos un plano de referencia:

```text
x mínimo = -500
x máximo = 500
y mínimo = -300
y máximo = 300
```

## 3. Definir intenciones permitidas

```text
goto: ir a una coordenada.
circle: trazar círculo.
stop: detener.
```

## 4. Prompt base

```text
Eres un intérprete de instrucciones para un robot móvil.
El espacio permitido es x=[-500,500], y=[-300,300].
Responde sólo JSON válido.
No uses markdown. No agregues explicación.
Schema:
{"intent":"goto|circle|stop","x":number|null,"y":number|null,"radius":number|null,"duration_s":number}
Instrucción: {instruccion}
```

## 5. Validar con Pydantic

```python
from pydantic import BaseModel, Field
from typing import Literal, Optional

class RobotCommand(BaseModel):
    intent: Literal["goto", "circle", "stop"]
    x: Optional[float] = Field(default=None, ge=-500, le=500)
    y: Optional[float] = Field(default=None, ge=-300, le=300)
    radius: Optional[float] = Field(default=None, ge=0, le=500)
    duration_s: float = Field(default=5, gt=0, le=120)
```

## 6. Pruebas mínimas

| Instrucción | Resultado esperado |
|---|---|
| Ve al centro | goto, x=0, y=0 |
| Detente | stop |
| Haz un círculo de radio 100 | circle, radius=100 |
| Ve a x=9999 | Rechazar por fuera de límite |
| Salta por la ventana | Rechazar por intención no permitida |

## 7. Qué documentar

- Prompt usado.
- JSON generado.
- Resultado de validación.
- Caso aceptado/rechazado.
- Explicación de cada rechazo.

## 8. Checklist

- [ ] Schema definido.
- [ ] Prompt documentado.
- [ ] 5 casos válidos.
- [ ] 5 casos inválidos.
- [ ] Evidencia de rechazo seguro.
