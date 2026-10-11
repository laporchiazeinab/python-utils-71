import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

def setup_logger(
    name: str = "autoclicker",
    log_file: Optional[str] = "logs/autoclicker.log",
    max_bytes: int = 1_048_576,
    backup_count: int = 3,
    level: int = logging.INFO
) -> logging.Logger:
    """Configures and returns a logger instance with rotating file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is initialized multiple times
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler for real-time autoclicker feedback
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating file handler for session logs
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
