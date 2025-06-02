from plyer import notification
import datetime
from paste_with_peace.config import load_config
import os

config = load_config()

def ensure_log_dir_exists(log_path):
    log_dir = os.path.dirname(log_path)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

def log_detection(label: str, text: str, log_file="logs/detection_log.txt", redact_mode="masked"):
    if not config["logging_enabled"]:
        return
    """Saves log of each time an alert is sent to logs/detection_log.txt"""
    clipped_text = ""
    print(redact_mode)
    if redact_mode == "masked":
        clipped_text = text[:5] + "*" * 10 + text[-5:]
    elif redact_mode == "hash":
        import hashlib
        clipped_text = f"hash={hashlib.sha256(text.encode()).hexdigest()}"
    elif redact_mode == "unchanged":
        clipped_text = (text[:40] + "...") if len(text) > 40 else text
    else:
        clipped_text = "[secret not logged]"
    timestamp = datetime.datetime.now().isoformat(timespec='seconds')

    log_path = config["log_file_path"]
    ensure_log_dir_exists(log_path)  # <-- Ensure the directory exists

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {label} | {clipped_text}\n")

def alert_secret_detected(label: str, _text: str):
    config = load_config()
    redact_mode = config.get("redact_mode", "masked")
    log_detection(label, _text, redact_mode=redact_mode)
    title = "⚠️ Paste with Peace: Potential Secret Detected"
    message = (
        f"Type: {label}\n"
        "The most recent item on your clipboard looks like something sensitive.\n"
        "PASTE WITH CAUTION"
    )
    notification.notify(
        title=title,
        message=message,
        timeout=config["popup_timeout"]  # Convert ms to seconds
    )