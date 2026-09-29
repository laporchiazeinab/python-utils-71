import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f8"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file with fallback to defaults.
    Returns a dictionary of validated application settings.
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Failed to load {filepath}: {e}. Using defaults.")
            
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """
    Saves current configuration state to a JSON file.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save {filepath}: {e}")