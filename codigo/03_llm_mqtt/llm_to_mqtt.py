import json, time, requests
import paho.mqtt.client as mqtt
from pydantic import BaseModel, Field, ValidationError
from typing import Literal, Optional

BROKER = "localhost"
TOPIC = "curso/robot/cmd"

class RobotCommand(BaseModel):
    intent: Literal["goto", "circle", "stop"]
    x: Optional[float] = Field(default=None, ge=-500, le=500)
    y: Optional[float] = Field(default=None, ge=-300, le=300)
    radius: Optional[float] = Field(default=None, ge=0, le=500)
    duration_s: Optional[float] = Field(default=5, gt=0, le=120)

def ask_llm(instruction: str) -> str:
    prompt = f"""
Eres un intérprete para robot móvil. Responde sólo JSON válido.
Schema: {{"intent":"goto|circle|stop","x":number|null,"y":number|null,"radius":number|null,"duration_s":number}}
Instrucción: {instruction}
"""
    r = requests.post("http://localhost:11434/api/generate", json={"model":"llama3.1:8b","prompt":prompt,"stream":False,"options":{"temperature":0.1}}, timeout=120)
    r.raise_for_status()
    return r.json()["response"]

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER, 1883, 60)
    while True:
        instruction = input("Instrucción> ").strip()
        if instruction.lower() in {"salir", "exit", "quit"}: break
        raw = ask_llm(instruction)
        print("LLM raw:", raw)
        try:
            cmd = RobotCommand.model_validate_json(raw)
        except ValidationError as e:
            print("RECHAZADO", e)
            continue
        payload = cmd.model_dump_json()
        client.publish(TOPIC, payload, qos=0, retain=False)
        print("PUBLICADO", TOPIC, payload)

if __name__ == "__main__": main()
