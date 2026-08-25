"""Validators for autoclicker parameters."""
import re
from typing import Any, Dict, Tuple, Optional

def validate_coordinates(x: int, y: int, max_width: int = 1920, max_height: int = 1080) -> bool:
    """Check if coordinates are within screen bounds."""
    if not isinstance(x, int) or not isinstance(y, int):
        return False
    return 0 <= x < max_width and 0 <= y < max_height

def validate_interval(interval: float) -> bool:
    """Validate time between clicks. 10ms to 60s."""
    if not isinstance(interval, (int, float)):
        return False
    return 0.01 <= interval <= 60.0

def validate_count(count: int) -> bool:
    """Positive integer for number of clicks."""
    if not isinstance(count, int):
        return False
    return count > 0

def validate_button(button: str) -> bool:
    """Standard mouse buttons only."""
    valid = {"left", "right", "middle"}
    return isinstance(button, str) and button.lower() in valid

def validate_hotkey(hotkey: str) -> bool:
    """Hotkey format e.g. ctrl+alt+s."""
    if not isinstance(hotkey, str) or not hotkey:
        return False
    parts = hotkey.lower().split("+")
    if len(parts) > 4:
        return False
    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789ctrlaltshiftwin")
    for part in parts:
        if not part or not all(c in allowed for c in part):
            return False
    return True

def validate_duration(duration: Optional[float]) -> bool:
    """Optional duration 0.5s to 2 hours."""
    if duration is None:
        return True
    if not isinstance(duration, (int, float)):
        return False
    return 0.5 <= duration <= 7200.0

def validate_config(config: Dict[str, Any]) -> Tuple[bool, str]:
    """Full config validation for autoclicker."""
    if not isinstance(config, dict):
        return False, "Must be dictionary"
    required = ["x", "y", "interval", "count", "button"]
    for key in required:
        if key not in config:
            return False, f"Missing {key}"
    if not validate_coordinates(config["x"], config["y"]):
        return False, "Bad coordinates"
    if not validate_interval(config["interval"]):
        return False, "Bad interval"
    if not validate_count(config["count"]):
        return False, "Bad count"
    if not validate_button(config["button"]):
        return False, "Bad button"
    if "hotkey" in config and not validate_hotkey(config["hotkey"]):
        return False, "Bad hotkey"
    if "duration" in config and not validate_duration(config.get("duration")):
        return False, "Bad duration"
    return True, "Valid"
class ConfigValidator:
    """Class for organized validation."""
    def __init__(self, width: int = 1920, height: int = 1080):
        self.width = width
        self.height = height
    def validate_position(self, x: int, y: int) -> bool:
        return validate_coordinates(x, y, self.width, self.height)
    def validate(self, config: Dict[str, Any]) -> Tuple[bool, str]:
        return validate_config(config)