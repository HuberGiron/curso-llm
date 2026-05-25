# Plantilla de prompt para visión robótica

Usa esta plantilla con un modelo multimodal:

```text
Observa la imagen del área de trabajo de un robot móvil.
Identifica obstáculos, zona libre y posibles riesgos.
Responde sólo JSON válido:
{
  "obstacle": true|false,
  "relative_position": "front|left|right|back|none",
  "confidence": 0.0,
  "recommended_action": "continue|stop|turn_left|turn_right"
}
No incluyas explicación.
```
