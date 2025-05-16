import pyperclip
import time
from paste_with_peace import scanner, notifier

def start_monitor(interval: float = 0.5):
    """Continuously check clipboard and scan new text."""
    print("[Paste with Peace] Clipboard monitor running...")
    last_text = ""

    while True:
        try:
            current_text = pyperclip.paste()

            # only have to check when we encounter new clipboard contents
            if current_text != last_text:
                last_text = current_text
                detected, label = scanner.is_potential_secret(current_text)

                if detected:
                    notifier.alert_secret_detected(label, current_text)

        except Exception as e:
            print(f"[monitor error] {e}")
        
        # only run as often as the interval says
        time.sleep(interval)

def scan_clipboard_text(text: str) -> bool:
    """Scan clipboard content directly (used for tests)."""
    detected, label = scanner.is_potential_secret(text)
    if detected:
        notifier.alert_secret_detected(label, text)
    return detected