import logging
import os
import sys

def setup_logger(name: str = 'autoclicker', log_file: str = 'app.log'):
    """Configures a robust logger with file rotation support."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    try:
        # Ensure directory existence
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (PermissionError, OSError) as e:
        # Fallback to console if file access is restricted
        print(f"Warning: Could not create log file at {log_file}: {e}", file=sys.stderr)
        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

# Global instance for autoclicker module
logger = setup_logger()