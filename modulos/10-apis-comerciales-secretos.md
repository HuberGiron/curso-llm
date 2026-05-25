---
title: "10. APIs comerciales, costos y secretos"
nav_order: 10
parent: "Módulos académicos"
---
# APIs comerciales, costos y secretos

## 1. Por qué usar APIs comerciales

Las APIs comerciales permiten acceder a modelos de alta capacidad sin comprar infraestructura propia. Son útiles para comparar el desempeño local contra modelos frontera, probar visión avanzada, integrar herramientas y estimar escenarios de adopción real.

## 2. Riesgos de uso académico

- Exposición de datos del proyecto.
- Costos variables.
- Cambios de modelos y precios.
- Dependencia de internet.
- Límites de tasa.
- Manejo incorrecto de API keys.

## 3. Regla crítica: nunca subir API keys

Las llaves deben vivir en variables de entorno o archivos `.env` que no se suben al repositorio.

`.gitignore`:

```text
.env
*.key
secrets.json
```

Python:

```python
import os
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Falta GEMINI_API_KEY")
```

## 4. Comparación conceptual

| Proveedor | Uso típico en el curso | Observaciones |
|---|---|---|
| OpenAI | Texto, herramientas, agentes, multimodalidad | Revisar Responses API y precios vigentes. |
| Gemini | Texto, visión, herramientas, video/audio según modelo | Buena opción para prácticas multimodales. |
| Claude | Razonamiento, documentación, tool use | Revisar límites y costos por modelo. |
| xAI Grok | Texto, visión, herramientas, tiempo real según disponibilidad | Revisar documentación actual antes de usar. |

## 5. Cálculo de costo

```python
def estimate_cost(input_tokens, output_tokens, in_price, out_price):
    return (input_tokens / 1_000_000) * in_price + (output_tokens / 1_000_000) * out_price

print(estimate_cost(400_000, 120_000, 0.50, 1.50))
```

## 6. Ejercicio

Cada equipo debe estimar el costo mensual de su proyecto final si se ejecuta:

- 100 instrucciones/día.
- 1,000 instrucciones/día.
- 10,000 instrucciones/día.

{: .evidencia }
> Entregar tabla con tokens promedio, costo por proveedor y recomendación de arquitectura local/comercial/híbrida.

## 7. Fuentes

- OpenAI API reference. <https://developers.openai.com/api/reference/overview/>
- OpenAI pricing. <https://openai.com/api/pricing/>
- Gemini API quickstart. <https://ai.google.dev/gemini-api/docs/quickstart>
- Gemini pricing. <https://ai.google.dev/gemini-api/docs/pricing>
- Anthropic pricing. <https://www.anthropic.com/pricing>
- xAI API docs. <https://docs.x.ai/overview>
