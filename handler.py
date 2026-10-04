import json
import os
from typing import Dict, Any

class ClickConfigHandler:
    """Handles loading and saving of autoclicker profiles."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath

    def load_profile(self) -> Dict[str, Any]:
        """Loads autoclicker settings from disk."""
        if not os.path.exists(self.filepath):
            return self._get_defaults()
        
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return self._get_defaults()

    def save_profile(self, data: Dict[str, Any]) -> bool:
        """Persists autoclicker settings to disk."""
        try:
            with open(self.filepath, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except IOError:
            return False

    def _get_defaults(self) -> Dict[str, Any]:
        """Default configuration for autoclicker runtime."""
        return {
            "interval": 0.1,
            "button": "left",
            "repeat": 0,
            "randomize": False
        }

def validate_click_data(data: Dict[str, Any]) -> bool:
    """Ensures configuration values are within safe bounds."""
    interval = data.get("interval", 0.1)
    return isinstance(interval, (int, float)) and interval > 0