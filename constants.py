import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'max_clicks': 100,
    'double_click': False,
    'enabled': True
}

def load_config(file_path):
    """Load configuration from a JSON file, using defaults if necessary."""
    if not os.path.exists(file_path):
        return DEFAULT_CONFIG
    with open(file_path, 'r') as file:
        try:
            config = json.load(file)
        except json.JSONDecodeError:
            return DEFAULT_CONFIG
    return {**DEFAULT_CONFIG, **config}

# Example usage:
# config = load_config('config.json')
# print(config)