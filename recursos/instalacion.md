---
layout: default
title: "Instalación y ambiente de trabajo"
parent: "Recursos"
nav_order: 2
---
# Instalación y ambiente de trabajo

## Software base

- Python 3.10 o superior.
- Visual Studio Code.
- Git.
- Ollama.
- Navegador moderno.
- Cliente MQTT o librería `paho-mqtt`.

## Ambiente Python

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r assets/code/requirements.txt
```

En macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r assets/code/requirements.txt
```

## Ollama

1. Instalar Ollama.
2. Descargar un modelo:

```bash
ollama pull llama3.1:8b
ollama pull gemma3:4b
```

3. Probar API local:

```bash
curl http://localhost:11434/api/generate -d '{"model":"llama3.1:8b","prompt":"Hola","stream":false}'
```

## Variables de entorno

Copiar `assets/code/.env.example` como `.env` y completar únicamente las llaves necesarias. No subir `.env` a GitHub.

## Fuentes

- [ollama_api](https://docs.ollama.com/api/introduction)
- [fastapi](https://fastapi.tiangolo.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [mqtt_oasis](https://www.oasis-open.org/standard/mqtt-v5-0-os/)