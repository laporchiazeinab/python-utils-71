import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "max_clicks": 100,
    "random_delay": True
}

def load_config(filepath: str = "config.json") -> dict:
    """Loads configuration from file with fallback to defaults."""
    if not os.path.exists(filepath):
        save_config(filepath, DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge with defaults to ensure all keys exist
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(filepath: str, config: dict) -> None:
    """Persists configuration dictionary to a JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")