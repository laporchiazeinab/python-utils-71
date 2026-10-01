import re
from typing import Dict, Any, Optional

def validate_click_config(config: Dict[str, Any]) -> bool:
    """Validates autoclicker configuration parameters for range and type."""
    required_keys = {"interval": float, "clicks": int, "button": str}
    
    # Check for missing keys
    if not all(key in config for key in required_keys):
        return False

    # Validate data types
    for key, expected_type in required_keys.items():
        if not isinstance(config[key], expected_type):
            return False

    # Validate business logic bounds
    if config["interval"] < 0.001:
        return False
    if config["clicks"] < -1:
        return False
    
    valid_buttons = {"left", "right", "middle"}
    if config["button"] not in valid_buttons:
        return False

    return True

def sanitize_hotkey_string(hotkey: str) -> Optional[str]:
    """Sanitizes and normalizes hotkey input strings."""
    if not isinstance(hotkey, str):
        return None
    
    cleaned = re.sub(r'[^a-zA-Z0-9+]', '', hotkey).lower()
    if not cleaned:
        return None
        
    return cleaned