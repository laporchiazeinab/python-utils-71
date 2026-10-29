import re

def validate_coordinate(x: int, y: int) -> bool:
    """Ensures mouse coordinates are within typical screen bounds."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_interval(interval: float) -> bool:
    """Checks if the click interval is physically realistic."""
    return isinstance(interval, (int, float)) and interval >= 0.01

def validate_key_binding(key: str) -> bool:
    """Verifies key string matches basic keyboard character standards."""
    return bool(re.match(r'^[a-zA-Z0-9]$', str(key)))

def sanitize_input(value: str) -> str:
    """Removes whitespace and forces lowercase for config parsing."""
    return str(value).strip().lower()

def validate_config_value(key: str, value: any) -> bool:
    """Routes values to specific validators based on key name."""
    validators = {
        'interval': validate_interval,
        'trigger_key': validate_key_binding
    }
    validator = validators.get(key)
    return validator(value) if validator else True