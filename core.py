import json
import os
from typing import Dict, Any

def save_clicker_profile(data: Dict[str, Any], filepath: str) -> bool:
    """Persists autoclicker configuration to a local JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        print(f"Storage operation failure: {e}")
        return False

def load_clicker_profile(filepath: str) -> Dict[str, Any]:
    """Retrieves autoclicker configuration from a local JSON file."""
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Data retrieval failure: {e}")
        return {}

def validate_config_schema(data: Dict[str, Any]) -> bool:
    """Checks if the profile data contains required keys."""
    required = {'interval', 'button', 'repeat'}
    return all(key in data for key in required)

def sanitize_coords(coords: Dict[str, int]) -> Dict[str, int]:
    """Ensures mouse coordinates remain within positive bounds."""
    return {
        'x': max(0, coords.get('x', 0)),
        'y': max(0, coords.get('y', 0))
    }