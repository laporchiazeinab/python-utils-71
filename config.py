from typing import Dict, Any, Optional
import json

class ConfigManager:
    """Handles loading and saving of autoclicker settings."""

    def __init__(self, filepath: str = "settings.json") -> None:
        self.filepath: str = filepath
        self.settings: Dict[str, Any] = {
            "interval": 0.1,
            "button": "left",
            "hotkey": "f6"
        }

    def load_config(self) -> Dict[str, Any]:
        """Reads configuration from a JSON file."""
        try:
            with open(self.filepath, "r") as f:
                self.settings.update(json.load(f))
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return self.settings

    def save_config(self, new_settings: Dict[str, Any]) -> None:
        """Persists updated configuration to disk."""
        self.settings.update(new_settings)
        with open(self.filepath, "w") as f:
            json.dump(self.settings, f, indent=4)

    def get_setting(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a specific setting value."""
        return self.settings.get(key, default)