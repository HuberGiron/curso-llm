"""Agente mínimo por skills.
La idea didáctica es separar: interpretar meta, validar acción, ejecutar skill y registrar evidencia.
"""
from dataclasses import dataclass, asdict
from typing import Callable
import time, json

@dataclass
class RobotState:
    x: float = 0
    y: float = 0
    status: str = 'idle'

state = RobotState()
log = []

def skill_goto(x: float, y: float):
    state.x, state.y, state.status = x, y, 'moving'
    time.sleep(0.2)
    state.status = 'idle'
    return {'ok': True, 'state': asdict(state)}

def skill_stop():
    state.status = 'stopped'
    return {'ok': True, 'state': asdict(state)}

skills: dict[str, Callable] = {'goto': skill_goto, 'stop': skill_stop}

def execute(action: dict):
    name = action.get('skill')
    if name not in skills:
        result = skills['stop']()
        result['warning'] = 'skill no permitida; se ejecutó stop'
    else:
        params = action.get('params', {})
        result = skills[name](**params)
    log.append({'t': time.time(), 'action': action, 'result': result})
    return result

if __name__ == '__main__':
    actions = [
        {'skill': 'goto', 'params': {'x': 100, 'y': 50}},
        {'skill': 'stop', 'params': {}}
    ]
    for a in actions:
        print(execute(a))
    print(json.dumps(log, indent=2))
