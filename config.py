from typing import Dict, Any, Optional

class Config:
    """Manages configuration settings for the autoclicker."""

    def __init__(self) -> None:
        self._settings: Dict[str, Any] = {
            "interval": 0.1,
            "button": "left",
            "enabled": False
        }

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a setting value by key."""
        return self._settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Update a specific configuration setting."""
        self._settings[key] = value

    @property
    def interval(self) -> float:
        """Get click interval in seconds."""
        return float(self._settings.get("interval", 0.1))

    @interval.setter
    def interval(self, value: float) -> None:
        """Set click interval with basic validation."""
        if value < 0.01:
            value = 0.01
        self._settings["interval"] = value

    def reset(self) -> None:
        """Reset configuration to default values."""
        self._settings = {
            "interval": 0.1,
            "button": "left",
            "enabled": False
        }