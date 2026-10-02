class AutoclickerError(Exception):
    """Base exception for the autoclicker project."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when the config file is missing or malformed."""
    pass

class ClickerExecutionError(AutoclickerError):
    """Raised when clicking operations fail due to hardware or OS."""
    pass

class HardwareInputError(ClickerExecutionError):
    """Raised when simulated input fails to register."""
    pass

def validate_os_support(platform_name: str):
    """Check if current OS is supported by the clicker."""
    supported = ['windows', 'linux', 'darwin']
    if platform_name.lower() not in supported:
        raise ConfigurationError(f"OS '{platform_name}' is not supported.")

def handle_critical_failure(e: Exception):
    """Standardized exit procedure for fatal application errors."""
    print(f"[FATAL] {type(e).__name__}: {e}")
    exit(1)