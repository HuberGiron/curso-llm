---
title: "5. Python y Ollama como API local"
nav_order: 5
parent: "Módulos académicos"
---
# Python y Ollama como API local

## 1. Objetivo técnico

Construir una interfaz mínima en Python capaz de enviar prompts a un modelo local mediante Ollama, recibir la respuesta y validar si la salida es útil para automatización.

## 2. Instalación mínima

```bash
ollama pull llama3.1:8b
ollama run llama3.1:8b
```

En otra terminal:

```bash
curl http://localhost:11434/api/generate -d '{"model":"llama3.1:8b","prompt":"Hola","stream":false}'
```

Si responde, la API local está funcionando.

## 3. Cliente Python mínimo

```python
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.1:8b",
    "prompt": "Responde sólo JSON: mueve el robot al centro",
    "stream": False,
    "options": {
        "temperature": 0.1,
        "num_predict": 120
    }
}

response = requests.post(OLLAMA_URL, json=payload, timeout=60)
response.raise_for_status()
print(response.json()["response"])
```

## 4. Validación de JSON

```python
import json

raw = response.json()["response"]
try:
    data = json.loads(raw)
except json.JSONDecodeError:
    print("Salida inválida")
else:
    print("JSON válido", data)
```

## 5. Reintento con prompt de reparación

Cuando la salida falla, no se debe mandar directamente al robot. Se puede hacer un reintento:

```python
repair_prompt = f"""
Convierte el siguiente texto en JSON válido con campos intent, x, y, duration_s.
No expliques nada. Texto: {raw}
"""
```

Sin embargo, el reintento no sustituye al validador. Para robótica, el backend debe rechazar cualquier comando fuera de límites.

## 6. Ejercicio guiado

1. Ejecutar un modelo local.
2. Enviar un prompt simple.
3. Medir el tiempo de respuesta.
4. Validar JSON.
5. Cambiar temperatura de 0.1 a 0.9.
6. Comparar estabilidad del formato.

{: .evidencia }
> Entregar código, capturas de terminal y tabla con al menos cinco pruebas por temperatura.

## 7. Código

El ejemplo completo está en:

```text
codigo/01_benchmark_ollama/
```

## 8. Fuente

- Ollama API: <https://docs.ollama.com/api/introduction>
