"""Constants and configuration defaults for the autoclicker module."""

from typing import Dict, Final, Tuple

# Click rate bounds (clicks per second)
MIN_CPS: Final[float] = 0.1
MAX_CPS: Final[float] = 1000.0
DEFAULT_CPS: Final[float] = 10.0

# Supported mouse input buttons
BUTTON_LEFT: Final[str] = "left"
BUTTON_RIGHT: Final[str] = "right"
BUTTON_MIDDLE: Final[str] = "middle"
VALID_BUTTONS: Final[Tuple[str, ...]] = (BUTTON_LEFT, BUTTON_RIGHT, BUTTON_MIDDLE)

# Click operation trigger modes
MODE_HOLD: Final[str] = "hold"
MODE_TOGGLE: Final[str] = "toggle"
MODE_BURST: Final[str] = "burst"
VALID_MODES: Final[Tuple[str, ...]] = (MODE_HOLD, MODE_TOGGLE, MODE_BURST)

# Default keyboard shortcut keybindings
DEFAULT_HOTKEYS: Final[Dict[str, str]] = {
    "start_stop": "F6",
    "toggle_hold": "F7",
    "emergency_stop": "Escape",
}

# Burst mode defaults
DEFAULT_BURST_COUNT: Final[int] = 5
MAX_BURST_COUNT: Final[int] = 500


def get_default_config() -> Dict[str, object]:
    """Generate a dictionary containing standard autoclicker default settings.

    Returns:
        Dict[str, object]: A fresh dictionary of default settings.
    """
    return {
        "cps": DEFAULT_CPS,
        "button": BUTTON_LEFT,
        "mode": MODE_TOGGLE,
        "burst_count": DEFAULT_BURST_COUNT,
        "hotkeys": DEFAULT_HOTKEYS.copy(),
    }
