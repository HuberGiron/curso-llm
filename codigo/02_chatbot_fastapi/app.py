from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles
    from pydantic import BaseModel
    import requests, time

    app = FastAPI(title="Chatbot local con Ollama")

    class ChatRequest(BaseModel):
        prompt: str
        model: str = "llama3.1:8b"
        temperature: float = 0.2
        robot_mode: bool = False

    @app.post("/chat")
    def chat(req: ChatRequest):
        system = ""
        if req.robot_mode:
            system = "Responde sólo JSON válido para un robot móvil. No uses markdown."
        prompt = f"{system}

Usuario: {req.prompt}" if system else req.prompt
        t0 = time.perf_counter()
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": req.model, "prompt": prompt, "stream": False, "options": {"temperature": req.temperature}},
            timeout=120,
        )
        r.raise_for_status()
        latency = time.perf_counter() - t0
        return {"response": r.json()["response"], "latency_s": round(latency, 3)}

    app.mount("/", StaticFiles(directory="static", html=True), name="static")
