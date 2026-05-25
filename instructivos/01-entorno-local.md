---
title: "1. Preparar entorno local"
nav_order: 1
parent: "Instructivos paso a paso"
---
# Preparar entorno local para LLM + robótica

## 1. Objetivo

Dejar lista una computadora para ejecutar modelos locales con Ollama, scripts de Python, APIs con FastAPI y pruebas de comunicación MQTT.

## 2. Instalaciones requeridas

- Git.
- Python 3.10 o superior.
- Visual Studio Code.
- Ollama.
- Mosquitto o broker MQTT disponible.
- Navegador moderno.

## 3. Verificar Python

```bash
python --version
pip --version
```

Crear entorno:

```bash
python -m venv .venv
```

Activar en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## 4. Instalar Ollama y modelo

```bash
ollama --version
ollama pull llama3.1:8b
ollama list
```

Prueba:

```bash
ollama run llama3.1:8b "Responde en una frase qué es un LLM"
```

## 5. Verificar API local

```bash
curl http://localhost:11434/api/generate -d "{"model":"llama3.1:8b","prompt":"hola","stream":false}"
```

Si falla:

- Revisar que Ollama esté abierto.
- Revisar puerto 11434.
- Probar otro modelo instalado.
- Revisar firewall.

## 6. Instalar dependencias del curso

```bash
pip install requests fastapi "uvicorn[standard]" paho-mqtt pydantic pandas matplotlib
```

## 7. Verificar MQTT local

Si usas Mosquitto:

```bash
mosquitto -v
```

En una terminal:

```bash
mosquitto_sub -h localhost -t curso/test
```

En otra:

```bash
mosquitto_pub -h localhost -t curso/test -m "hola"
```

## 8. Checklist de entorno

- [ ] Python responde en terminal.
- [ ] Entorno virtual creado.
- [ ] Ollama instalado.
- [ ] Modelo descargado.
- [ ] API de Ollama responde.
- [ ] FastAPI instalado.
- [ ] MQTT probado con publish/subscribe.
- [ ] Capturas guardadas para reporte.
