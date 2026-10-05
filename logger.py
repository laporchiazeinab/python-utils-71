import logging
import sys
from datetime import datetime

def setup_logger(name: str, log_file: str = "autoclicker.log", level: int = logging.INFO) -> logging.Logger:
    """Configures a standardized logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # File handler for persistent logs
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Stream handler for console output
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

def log_event(logger: logging.Logger, message: str, level: str = "info") -> None:
    """Helper to dispatch logs based on priority level."""
    levels = {
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "debug": logger.debug
    }
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)