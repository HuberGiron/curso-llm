"""Benchmark básico para modelos en Ollama.
Mide latencia total y guarda resultados en CSV.
Uso:
  python benchmark_ollama.py --model llama3.1:8b --n 10 --prompt "Resume MQTT en 3 líneas"
"""
import argparse, csv, time, requests
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='llama3.1:8b')
parser.add_argument('--n', type=int, default=5)
parser.add_argument('--prompt', default='Explica qué es un LLM en una frase.')
parser.add_argument('--host', default='http://localhost:11434')
args = parser.parse_args()

rows = []
for i in range(args.n):
    t0 = time.perf_counter()
    r = requests.post(f'{args.host}/api/generate', json={
        'model': args.model,
        'prompt': args.prompt,
        'stream': False,
        'options': {'temperature': 0.2, 'num_predict': 128}
    }, timeout=120)
    r.raise_for_status()
    dt = time.perf_counter() - t0
    data = r.json()
    rows.append({
        'timestamp': datetime.now().isoformat(timespec='seconds'),
        'model': args.model,
        'trial': i + 1,
        'latency_s': round(dt, 4),
        'eval_count': data.get('eval_count', ''),
        'prompt_eval_count': data.get('prompt_eval_count', ''),
        'response_preview': (data.get('response') or '')[:120].replace('\n', ' ')
    })
    print(rows[-1])

out = f'benchmark_{args.model.replace(":", "_")}.csv'
with open(out, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
print(f'Archivo guardado: {out}')
