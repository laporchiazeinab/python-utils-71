import platform

# Application configuration constants
APP_NAME = "python-utils-71"
VERSION = "1.0.0"

# Click simulation constants
DEFAULT_INTERVAL = 0.1  # Seconds between clicks
MIN_INTERVAL = 0.01
MAX_INTERVAL = 10.0

# Coordinate system definitions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Key identifiers for input control
START_KEY = 'f8'
STOP_KEY = 'f9'
EXIT_KEY = 'esc'

# Operating system identification
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"
IS_LINUX = platform.system() == "Linux"

# Data handling constants for autoclicker profiles
PROFILE_DIR = "./profiles"
DEFAULT_CONFIG_FILE = "config.json"

# Error codes for exception handling
ERR_INVALID_COORDINATES = 1001
ERR_PERMISSION_DENIED = 1002
ERR_CONFIG_LOAD_FAILURE = 1003