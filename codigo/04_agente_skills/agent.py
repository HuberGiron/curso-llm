"""Agente mínimo con skills cerradas. No ejecuta herramientas fuera de la lista."""
import json
from dataclasses import dataclass

ROBOT_STATE = {"x": 0.0, "y": 0.0, "status": "idle"}

def goto(x: float, y: float, duration_s: float = 5.0):
    if not (-500 <= x <= 500 and -300 <= y <= 300):
        return {"ok": False, "error": "fuera_de_limites"}
    ROBOT_STATE.update({"x": x, "y": y, "status": "moving"})
    return {"ok": True, "state": ROBOT_STATE}

def stop():
    ROBOT_STATE["status"] = "stopped"
    return {"ok": True, "state": ROBOT_STATE}

def get_state():
    return {"ok": True, "state": ROBOT_STATE}

SKILLS = {"goto": goto, "stop": stop, "get_state": get_state}

def execute(action_json: str):
    action = json.loads(action_json)
    name = action.get("skill")
    args = action.get("args", {})
    if name not in SKILLS:
        return {"ok": False, "error": "skill_no_permitida"}
    return SKILLS[name](**args)

if __name__ == "__main__":
    plan = [
        '{"skill":"goto","args":{"x":0,"y":0,"duration_s":5}}',
        '{"skill":"get_state","args":{}}',
        '{"skill":"stop","args":{}}'
    ]
    for step in plan:
        print("ACTION", step)
        print("RESULT", execute(step))
