import json
import os
import sys

DEFAULT_CONFIG = {
    "logging_enabled": True,
    "log_file_path": "logs/detection_log.txt",
    "popup_timeout": 5,
    "redact_mode": "masked",
    "allow_user_quit": False,
    "clear_after_paste": False,
    "enabled_apps": {
        "slack": True
    }
}

def get_config_path():
    if getattr(sys, 'frozen', False):
        # Running from a PyInstaller onefile bundle
        base_path = os.path.dirname(sys.executable)
    else:
        # Running from source
        # base_path = os.path.dirname(os.path.dirname(__file__))  # go up one level
        base_path = os.path.dirname(__file__)  # current directory
    return os.path.join(base_path, "config.json")

def load_config():
    """Loads config settings from config.json (merged with defaults)."""
    path = get_config_path()
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
        return {**DEFAULT_CONFIG, **user_config}
    return DEFAULT_CONFIG

def save_config(updated_config):
    """Writes updated settings to config.json."""
    path = get_config_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(updated_config, f, indent=4)
