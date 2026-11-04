import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat_count": 0
}

def load_config(filepath="config.json"):
    """Loads configuration from file with defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(config, filepath="config.json"):
    """Persists current configuration to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError:
        pass

if __name__ == "__main__":
    # Example usage for verification
    settings = load_config()
    print(f"Active settings: {settings}")