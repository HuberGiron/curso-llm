import argparse, csv, json, statistics, time
    from pathlib import Path
    import requests

    def call_ollama(model: str, prompt: str, temperature: float, num_predict: int):
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": temperature, "num_predict": num_predict},
        }
        t0 = time.perf_counter()
        r = requests.post("http://localhost:11434/api/generate", json=payload, timeout=120)
        dt = time.perf_counter() - t0
        r.raise_for_status()
        data = r.json()
        return dt, data.get("response", ""), data

    def is_json(text: str) -> bool:
        try:
            json.loads(text)
            return True
        except Exception:
            return False

    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("--model", default="llama3.1:8b")
        ap.add_argument("--prompt", default='Devuelve sólo JSON: ve al centro en 5 segundos')
        ap.add_argument("--runs", type=int, default=10)
        ap.add_argument("--temperature", type=float, default=0.1)
        ap.add_argument("--num-predict", type=int, default=120)
        ap.add_argument("--out", default="benchmark_results.csv")
        args = ap.parse_args()

        rows = []
        for i in range(args.runs):
            try:
                dt, text, raw = call_ollama(args.model, args.prompt, args.temperature, args.num_predict)
                rows.append({
                    "run": i+1,
                    "model": args.model,
                    "temperature": args.temperature,
                    "latency_s": round(dt, 4),
                    "json_valid": is_json(text),
                    "response_chars": len(text),
                    "response": text.replace("
", "\n")[:500],
                })
                print(f"[{i+1}/{args.runs}] {dt:.3f}s json={rows[-1]['json_valid']}")
            except Exception as e:
                rows.append({"run": i+1, "model": args.model, "temperature": args.temperature, "latency_s": None, "json_valid": False, "response_chars": 0, "response": f"ERROR: {e}"})
                print(f"[{i+1}/{args.runs}] ERROR {e}")

        out = Path(args.out)
        with out.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader(); writer.writerows(rows)
        ok_times = [r["latency_s"] for r in rows if isinstance(r["latency_s"], float)]
        if ok_times:
            print("mean latency:", statistics.mean(ok_times))
            print("json success:", sum(r["json_valid"] for r in rows), "/", len(rows))
        print("saved", out)

    if __name__ == "__main__":
        main()
