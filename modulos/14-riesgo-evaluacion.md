---
title: "14. Evaluación, seguridad y prospectiva de adopción"
nav_order: 14
parent: "Módulos académicos"
---
# Evaluación, seguridad y prospectiva de adopción

## 1. Evaluar un prototipo LLM-robótico

Un prototipo académico no debe evaluarse sólo por funcionar una vez. Debe evaluarse por repetibilidad, límites y fallas. La evaluación mínima debe incluir:

- Casos normales.
- Casos ambiguos.
- Casos fuera de rango.
- Casos adversarios simples.
- Desconexión de broker o API.
- Respuesta lenta del modelo.
- Salida inválida.

## 2. Matriz de riesgo

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---:|---:|---|
| JSON inválido | Media | Media | Validador + reintento. |
| Comando peligroso | Baja-media | Alta | Límites, paro, whitelist. |
| API key expuesta | Media | Alta | `.env`, rotación, GitHub secret scanning. |
| Latencia excesiva | Alta | Media | Modelo local menor, cache, prompt corto. |
| Alucinación de herramienta | Media | Alta | Lista cerrada de skills. |

## 3. Prospectiva de adopción

Para cerrar el curso, cada equipo debe argumentar qué tan viable es su propuesta en tres horizontes:

- **Hoy:** prototipo académico con restricciones.
- **1–2 años:** integración en laboratorios, simuladores o HMIs inteligentes.
- **3–5 años:** sistemas semiautónomos con agentes multimodales, visión, herramientas y validación robusta.

## 4. Criterio académico

Una conclusión sólida debe distinguir entre demostración y adopción. Que un LLM controle un robot en un demo no implica que sea listo para producción. La adopción requiere confiabilidad, trazabilidad, seguridad, costos sostenibles y responsabilidad institucional.

## 5. Fuentes

- NIST AI Risk Management Framework. <https://www.nist.gov/itl/ai-risk-management-framework>
- NIST Generative AI Profile. <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf>
- RT-2. <https://arxiv.org/abs/2307.15818>
