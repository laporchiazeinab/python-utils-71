import logging
import os
from datetime import datetime

# Configure logger for autoclicker runtime tracking
logger = logging.getLogger('autoclicker')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def safe_log_action(message: str):
    """Logs user actions with filesystem boundary checks."""
    try:
        if not isinstance(message, str):
            raise ValueError('Log message must be a string')
        
        # Verify log directory integrity
        if not os.path.exists('app.log') and not os.access('.', os.W_OK):
            print(f'CRITICAL: Cannot write log to disk: {message}')
            return
        
        logger.info(message)
    except (OSError, ValueError) as e:
        # Fail silently to avoid interrupting click loop
        print(f'Logger failure: {e}')

def log_exception(exc: Exception):
    """Formats and records exceptions for debug persistence."""
    timestamp = datetime.now().isoformat()
    error_msg = f'[{timestamp}] CRITICAL ERROR: {type(exc).__name__} - {str(exc)}'
    
    try:
        with open('error.log', 'a') as f:
            f.write(error_msg + '\n')
    except Exception:
        # Last-resort console fallback for critical disk errors
        print(f'Fatal error logger failure: {error_msg}')