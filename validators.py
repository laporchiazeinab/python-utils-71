from typing import Any, Dict, Tuple


def validate_click_interval(interval: float, min_interval: float = 0.001) -> float:
    """Validate and clamp the click interval in seconds."""
    if not isinstance(interval, (int, float)):
        raise TypeError("Interval must be a numeric value.")
    if interval < min_interval:
        raise ValueError(f"Interval cannot be less than {min_interval} seconds.")
    return float(interval)


def validate_coordinates(coords: Tuple[int, int], screen_size: Tuple[int, int] = (3840, 2160)) -> Tuple[int, int]:
    """Ensure x and y coordinates fall within screen boundaries."""
    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        raise TypeError("Coordinates must be a tuple or list of (x, y).")
    x, y = coords
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Coordinate values must be integers.")
    max_w, max_h = screen_size
    if not (0 <= x <= max_w and 0 <= y <= max_h):
        raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds [0-{max_w}, 0-{max_h}].")
    return (x, y)


def validate_profile_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Validate autoclicker profile data dictionary."""
    required = {"click_type", "interval", "repeat_count"}
    missing = required - set(config.keys())
    if missing:
        raise KeyError(f"Missing required profile keys: {', '.join(missing)}")
    
    valid_buttons = {"left", "right", "middle"}
    if config["click_type"] not in valid_buttons:
        raise ValueError(f"Invalid click_type. Must be one of {valid_buttons}")
    
    validate_click_interval(config["interval"])
    
    repeat = config["repeat_count"]
    if not isinstance(repeat, int) or repeat < 0:
        raise ValueError("repeat_count must be a non-negative integer.")
        
    return config
