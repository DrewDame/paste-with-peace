from plyer import notification

def alert_secret_detected(label: str, _text: str):
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