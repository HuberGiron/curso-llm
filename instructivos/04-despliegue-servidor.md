---
title: "4. Despliegue básico en servidor"
nav_order: 4
parent: "Instructivos paso a paso"
---
# Despliegue básico en servidor

## 1. Objetivo

Comprender cómo pasar de un prototipo local a un backend desplegado en servidor, cuidando seguridad de API keys y separación frontend/backend.

## 2. Arquitectura recomendada

```text
Navegador → HTTPS/Nginx → FastAPI/Uvicorn → LLM local o API comercial
```

## 3. Variables de entorno

Crear archivo `.env` sólo en servidor:

```text
GEMINI_API_KEY=...
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
```

Nunca subir `.env` a GitHub.

## 4. Servicio FastAPI

Ejecución de prueba:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## 5. Nginx como proxy

Ejemplo conceptual:

```nginx
server {
    server_name ejemplo.tudominio.mx;
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 6. Criterios mínimos de seguridad

- HTTPS activo.
- API keys en variables de entorno.
- CORS limitado al dominio real.
- Logs sin secretos.
- Límite de tamaño de prompt.
- Autenticación si el endpoint ejecuta acciones.

## 7. Checklist

- [ ] Backend corre localmente.
- [ ] Backend corre en servidor.
- [ ] Nginx redirige correctamente.
- [ ] HTTPS activo.
- [ ] `.env` no está en GitHub.
- [ ] CORS configurado.
- [ ] Prueba de endpoint documentada.
