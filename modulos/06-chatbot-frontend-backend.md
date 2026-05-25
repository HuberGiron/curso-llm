---
title: "6. Chatbot local con frontend y backend"
nav_order: 6
parent: "Módulos académicos"
---
# Chatbot local con Frontend y Backend

## 1. Arquitectura

Un chatbot académico mínimo debe separar responsabilidades:

```text
HTML/CSS/JS → FastAPI → Ollama → FastAPI → HTML/CSS/JS
```

Esta separación permite cambiar la interfaz sin tocar el modelo, cambiar el modelo sin tocar la interfaz y registrar métricas en el backend.

## 2. Backend con FastAPI

FastAPI permite crear APIs HTTP en Python con tipado y documentación automática. El endpoint mínimo recibe un prompt y devuelve respuesta.

```python
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str
    model: str = "llama3.1:8b"

@app.post("/chat")
def chat(req: ChatRequest):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": req.model, "prompt": req.prompt, "stream": False},
        timeout=60
    )
    r.raise_for_status()
    return {"response": r.json()["response"]}
```

## 3. Frontend mínimo

```html
<input id="prompt" placeholder="Escribe una instrucción">
<button onclick="sendPrompt()">Enviar</button>
<pre id="out"></pre>
<script>
async function sendPrompt(){
  const prompt = document.getElementById('prompt').value;
  const r = await fetch('/chat', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({prompt})
  });
  const data = await r.json();
  document.getElementById('out').textContent = data.response;
}
</script>
```

## 4. Variables experimentales

El mismo chatbot se usará para probar:

- Temperatura.
- Máximo de tokens.
- Prompt de sistema.
- Modelo local.
- Tiempo total de respuesta.
- Calidad de salida.

## 5. Riesgos y buenas prácticas

- No exponer Ollama directamente a internet sin seguridad.
- No guardar API keys en JavaScript del navegador.
- Registrar errores del backend.
- Limitar tamaño de prompt.
- Validar salidas antes de usarlas como comandos.

## 6. Práctica en clase

Construir un chatbot local que pueda trabajar en dos modos:

1. Modo conversación general.
2. Modo robot, donde la salida debe ser JSON.

{: .evidencia }
> Entregar repositorio con backend, frontend, capturas, instrucciones de ejecución y tres ejemplos de conversación.

## 7. Fuentes

- FastAPI tutorial. <https://fastapi.tiangolo.com/tutorial/first-steps/>
- Ollama API. <https://docs.ollama.com/api/introduction>
