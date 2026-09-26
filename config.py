import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "delay": 0.1,          # delay between clicks in seconds
    "button": "left",      # 'left', 'right', 'middle'
    "click_type": "single",# 'single', 'double'
    "hotkey_start": "f6",  # start clicking hotkey
    "hotkey_stop": "f7"    # stop clicking hotkey
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from JSON file or creates it with defaults."""
        if not os.path.exists(self.filepath):
            self._save_defaults()
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.filepath, "r") as f:
                user_config = json.load(f)
            
            # Merge user config with defaults to handle missing keys and type safety
            config = DEFAULT_CONFIG.copy()
            for key, value in user_config.items():
                if key in DEFAULT_CONFIG and isinstance(value, type(DEFAULT_CONFIG[key])):
                    config[key] = value
            return config
        except (json.JSONDecodeError, IOError):
            # Fallback to default config on parse or read errors
            return DEFAULT_CONFIG.copy()

    def _save_defaults(self) -> None:
        """Saves default configuration to disk to guide the user."""
        try:
            with open(self.filepath, "w") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        except IOError:
            pass

    def get(self, key: str) -> Any:
        """Retrieve a configuration value by key with safe fallback."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))