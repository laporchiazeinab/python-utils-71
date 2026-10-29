import platform
from dataclasses import dataclass

# autoclicker configuration defaults
DEFAULT_INTERVAL = 0.1
DEFAULT_BUTTON = 'left'
DEFAULT_MAX_CLICKS = 0  # 0 represents infinite

# system specific key identifiers
IS_WINDOWS = platform.system() == 'Windows'

@dataclass(frozen=True)
class ClickEvent:
    """structure for autoclicker input events"""
    x: int
    y: int
    button: str
    interval: float
    max_clicks: int

# preset delay boundaries in seconds
MIN_DELAY = 0.001
MAX_DELAY = 60.0

# default mouse coordinate validation
SCREEN_BOUNDS = {
    'min_x': 0,
    'min_y': 0,
    'max_x': 1920,
    'max_y': 1080
}

def get_default_config() -> ClickEvent:
    """utility to return baseline configuration"""
    return ClickEvent(
        x=0,
        y=0,
        button=DEFAULT_BUTTON,
        interval=DEFAULT_INTERVAL,
        max_clicks=DEFAULT_MAX_CLICKS
    )