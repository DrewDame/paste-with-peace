from plyer import notification

def alert_secret_detected(label: str, _text: str):
    message = f"Possible secret detected: {label}"
    notification.notify(
        title="Paste with Peace",
        message=message,
        timeout=5
    )