---
title: "3. Modelos abiertos, comerciales, Hugging Face y Ollama"
nav_order: 3
parent: "Módulos académicos"
---
# Modelos abiertos, comerciales, Hugging Face y Ollama

## 1. Criterios de clasificación

En un curso de prospectiva no basta con preguntar “¿qué modelo es mejor?”. La pregunta correcta es: ¿mejor para qué escenario, con qué restricciones y bajo qué costo? Para sistemas de automatización se recomienda comparar modelos con estos criterios:

| Criterio | Relevancia técnica |
|---|---|
| Calidad de instrucciones | Capacidad para seguir formato, idioma y restricciones. |
| Latencia | Tiempo hasta primera respuesta y tiempo total. |
| Costo | Precio por tokens, infraestructura local o suscripción. |
| Privacidad | Si los datos salen del laboratorio o permanecen localmente. |
| Conectividad | Dependencia de internet o APIs externas. |
| Tool use | Capacidad para usar funciones, herramientas o JSON estructurado. |
| Visión | Soporte para imágenes, cámara o percepción visual. |
| Licencia | Permisos para uso académico, investigación o comercial. |

## 2. Modelos comerciales

Los modelos comerciales suelen ofrecer alta calidad, APIs estables, modelos multimodales y mantenimiento continuo. Su restricción principal es costo, dependencia del proveedor y exposición de datos a servicios externos. En automatización, conviene usarlos cuando se necesita alta capacidad lingüística o visión avanzada, pero no para control duro de tiempo real.

Ejemplos de familias comerciales actuales:

- OpenAI: modelos vía Responses API y Chat Completions.
- Google Gemini: modelos con capacidades de texto, imagen, audio, video y herramientas.
- Anthropic Claude: modelos orientados a conversación, razonamiento, herramientas y seguridad.
- xAI Grok: modelos accesibles vía API para texto, visión, herramientas y voz.

## 3. Modelos abiertos o de pesos disponibles

Los modelos abiertos o de pesos disponibles permiten ejecución local, evaluación reproducible y menor dependencia de servicios externos. En el curso se recomienda probar modelos de tamaño 4B a 12B para computadoras con GPU moderada, y comparar contra APIs comerciales.

Ejemplos útiles para clase:

- Llama 3.1 / familias Llama.
- Mistral / Mixtral / Devstral.
- Gemma.
- Qwen.
- Phi.

La selección debe hacerse con pruebas. Un modelo pequeño puede ser mejor que uno grande si sigue mejor el formato JSON o si corre con latencia menor en el hardware disponible.

## 4. Hugging Face como ecosistema académico

Hugging Face funciona como repositorio de modelos, datasets, espacios de demostración y documentación. Para uso académico es importante revisar:

- **Model card:** descripción, arquitectura, licencia, usos previstos y limitaciones.
- **Tamaño y formato:** PyTorch, Safetensors, GGUF, cuantizaciones.
- **Idiomas:** desempeño esperado en español.
- **Tareas soportadas:** texto, visión, embeddings, tool calling.
- **Restricciones de licencia:** investigación, comercial, redistribución.

## 5. Ollama como interfaz local

Ollama simplifica la ejecución local de modelos. Una vez instalado, expone una API local en:

```text
http://localhost:11434/api
```

Ejemplo con `curl`:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.1:8b",
  "prompt": "Devuelve JSON para ir al centro del plano"
}'
```

Ejemplo con Python:

```python
import requests

payload = {
    "model": "llama3.1:8b",
    "prompt": "Devuelve JSON: ve al centro en 5 segundos",
    "stream": False
}

r = requests.post("http://localhost:11434/api/generate", json=payload, timeout=60)
print(r.json()["response"])
```

## 6. Ejercicio de selección de modelo

Cada equipo debe elegir tres modelos y justificar su selección:

1. Uno local pequeño.
2. Uno local mediano.
3. Uno comercial o remoto.

Criterios mínimos: latencia, costo, idioma, formato JSON, privacidad y compatibilidad con el proyecto final.

{: .evidencia }
> Entregar tabla comparativa con modelo, proveedor, tamaño, licencia, costo estimado, hardware requerido y evidencia de una prueba simple.

## 7. Fuentes

- Ollama API. <https://docs.ollama.com/api/introduction>
- Hugging Face Hub. <https://huggingface.co/docs/hub/en/index>
- Meta Llama model cards. <https://www.llama.com/docs/model-cards-and-prompt-formats/>
- Mistral model overview. <https://docs.mistral.ai/models/overview>
- OpenAI API. <https://developers.openai.com/api/reference/overview/>
- Gemini API. <https://ai.google.dev/gemini-api/docs/quickstart>
