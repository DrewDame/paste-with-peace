import json
import os

DEFAULT_CONFIG = {
  "logging_enabled": True,
  "log_file_path": "logs/detection_log.txt",
  "popup_timeout": 5,
  "redact_mode": "masked",
  "allow_user_quit": False,
}

def load_config(path="config.json"):
    """Loads config settings from config.json"""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
        return {**DEFAULT_CONFIG, **user_config}
    return DEFAULT_CONFIG