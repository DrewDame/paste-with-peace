from plyer import notification
import datetime

def log_detection(label: str, text: str, log_file="logs/detection_log.txt", redact_mode="masked"):
    """Saves log of each time an alert is sent to logs/detection_log.txt"""
    clippted_text = ""
    if redact_mode == "masked":
        clipped_text = text[:5] + "*" * 10 + text[-5:]
    elif redact_mode == "hash":
        clipped_text = f"hash={hashlib.sha256(text.encode()).hexdigest()}"
    elif redact_mode == "unchanged":
        clipped_text = (text[:40] + "...") if len(text) > 40 else text
    else:
        clipped_text = "[secret not logged]"
    timestamp = datetime.datetime.now().isoformat(timespec='seconds')

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {label} | {clipped_text}\n")

def alert_secret_detected(label: str, _text: str):
    log_detection(label, _text)
    title = "⚠️ Paste with Peace: Potential Secret Detected"
    message = (
        f"Type: {label}\n"
        "The most recent item on your clipboard looks like something sensitive.\n"
        "PASTE WITH CAUTION"
    )
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )