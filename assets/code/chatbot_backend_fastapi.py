"""Backend mínimo para chatbot local con Ollama.
Ejecutar:
  uvicorn chatbot_backend_fastapi:app --reload --port 8000
"""
import os, time, requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama3.1:8b')

app = FastAPI(title='Chatbot LLM local')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], allow_credentials=True,
    allow_methods=['*'], allow_headers=['*'],
)

class ChatRequest(BaseModel):
    prompt: str
    temperature: float = 0.2
    max_tokens: int = 256

@app.post('/chat')
def chat(req: ChatRequest):
    t0 = time.perf_counter()
    payload = {
        'model': OLLAMA_MODEL,
        'prompt': req.prompt,
        'stream': False,
        'options': {'temperature': req.temperature, 'num_predict': req.max_tokens}
    }
    r = requests.post(f'{OLLAMA_BASE_URL}/api/generate', json=payload, timeout=120)
    r.raise_for_status()
    data = r.json()
    return {
        'model': OLLAMA_MODEL,
        'response': data.get('response', ''),
        'latency_s': round(time.perf_counter() - t0, 4),
        'eval_count': data.get('eval_count'),
        'prompt_eval_count': data.get('prompt_eval_count')
    }
