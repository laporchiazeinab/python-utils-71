import json
import os

DEFAULT_CONFIG = {
    "cps": 10,
    "hotkey": "f6",
    "button": "left",
    "hold_time": 0.05,
    "sound_enabled": False
}

class ConfigLoader:
    def __init__(self, filepath="config.json"):
        self.filepath = filepath
        self.config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self):
        """Load configuration from file or create with defaults if missing."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            except (json.JSONDecodeError, IOError):
                # Fallback to defaults on corrupt file
                self.save()
        else:
            self.save()

    def save(self):
        """Save current configuration to disk."""
        try:
            with open(self.filepath, "w") as f:
                json.dump(self.config, f, indent=4)
        except IOError:
            pass

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self.config[key] = value
        self.save()
