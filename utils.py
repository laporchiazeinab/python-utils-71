import json
import os
from typing import Dict, Any

def load_clicker_profile(filepath: str) -> Dict[str, Any]:
    """Reads and parses clicker settings from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "loop": True}
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_clicker_profile(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists clicker settings to disk safely."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_settings(settings: Dict[str, Any]) -> bool:
    """Checks integrity of click interval and constraints."""
    interval = settings.get("interval", 0.0)
    if not isinstance(interval, (int, float)) or interval < 0.01:
        return False
    return settings.get("button") in ["left", "right", "middle"]
