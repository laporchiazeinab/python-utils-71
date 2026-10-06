import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from JSON file or returns defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(file_path):
        return config
        
    try:
        with open(file_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Saves configuration dictionary to a JSON file."""
    try:
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")