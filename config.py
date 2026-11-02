import json
import os
from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "cps": 10.0,
    "mouse_button": "left",
    "hotkey": "f6",
    "click_type": "single",
    "randomize_interval": True,
    "jitter_range": 0.015,
    "max_clicks": 0,
}

class ConfigLoader:
    """Handles loading, validating, and saving autoclicker configurations."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path

    def load(self) -> Dict[str, Any]:
        """Load configuration from JSON file, merging with default values."""
        config = DEFAULT_CONFIG.copy()
        if not os.path.exists(self.config_path):
            self.save(config)
            return config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    config.update(user_config)
        except (json.JSONDecodeError, OSError):
            pass

        return self._sanitize(config)

    def save(self, config: Dict[str, Any]) -> bool:
        """Save configuration dictionary to JSON file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=4)
            return True
        except OSError:
            return False

    def _sanitize(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Ensure configuration parameters stay within safe runtime limits."""
        config["cps"] = max(0.1, min(100.0, float(config.get("cps", 10.0))))
        config["jitter_range"] = max(0.0, min(1.0, float(config.get("jitter_range", 0.015))))
        if config.get("mouse_button") not in ("left", "right", "middle"):
            config["mouse_button"] = "left"
        return config
