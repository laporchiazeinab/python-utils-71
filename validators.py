"""Click configuration validation utilities for autoclicker application."""

from typing import Any, Dict, Optional, Tuple

VALID_BUTTONS = {"left", "right", "middle"}


def validate_cps(cps: float) -> float:
    """Validate clicks-per-second value within a safe range."""
    cps_float = float(cps)
    if cps_float <= 0 or cps_float > 1000:
        raise ValueError("CPS must be greater than 0 and at most 1000")
    return round(cps_float, 2)


def validate_coordinates(
    coords: Tuple[int, int], screen_bounds: Optional[Tuple[int, int]] = None
) -> Tuple[int, int]:
    """Validate target click screen coordinates."""
    x, y = int(coords[0]), int(coords[1])
    if x < 0 or y < 0:
        raise ValueError("Screen coordinates must be non-negative integers")

    if screen_bounds:
        max_x, max_y = screen_bounds
        if x > max_x or y > max_y:
            raise ValueError(f"Coordinates ({x}, {y}) exceed bounds ({max_x}, {max_y})")

    return (x, y)


def validate_click_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Validate complete autoclicker configuration dictionary."""
    if not isinstance(config, dict):
        raise TypeError("Configuration must be a dictionary")

    validated = {}

    cps = config.get("cps", 10.0)
    validated["cps"] = validate_cps(cps)

    button = str(config.get("button", "left")).lower()
    if button not in VALID_BUTTONS:
        raise ValueError(f"Invalid mouse button: {button}. Must be one of {VALID_BUTTONS}")
    validated["button"] = button

    if "coords" in config and config["coords"] is not None:
        validated["coords"] = validate_coordinates(config["coords"])
    else:
        validated["coords"] = None

    repeat = config.get("repeat", 0)
    if not isinstance(repeat, int) or repeat < 0:
        raise ValueError("Repeat count must be a non-negative integer")
    validated["repeat"] = repeat

    return validated
