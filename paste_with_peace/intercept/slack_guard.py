import time
import threading
import pyperclip
import keyboard
import pygetwindow as gw
import pyautogui
from paste_with_peace.config import load_config
from paste_with_peace import scanner, notifier

# currently only works on windows

pyautogui.PAUSE = 0
config = load_config()
enter_blocked = False

def delete_pasted_content():
    pasted_text = pyperclip.paste()
    length = len(pasted_text)

    # Add a small buffer in case Slack auto-formats (like with spaces or quotes)
    # num_presses = min(length + 3, 100)  # Avoid going crazy
    num_presses = length

    time.sleep(0.1)
    for _ in range(num_presses):
        pyautogui.press('backspace')
        # time.sleep(0.01)

def is_slack_active_window() -> bool:
    """Returns true if Slack is the active window"""
    try:
        active_window = gw.getActiveWindow()
        return active_window and "Slack" in active_window.title
    except Exception:
        return False

def clipboard_has_secret() -> tuple[bool, str, str]:
    """Returns true if there is sensitive information on the clipboard"""
    text = pyperclip.paste()
    detected, label = scanner.is_potential_secret(text)
    return detected, label, text

def block_enter_temporarily():
    """Blocks enter key indefinitely"""
    global enter_blocked
    if not enter_blocked:
        enter_blocked = True
        keyboard.block_key('enter')
        print('Blocked Enter key')

def unblock_enter():
    """Unblocks enter key indefinitely"""
    global enter_blocked
    if enter_blocked:
        enter_blocked = False
        keyboard.unblock_key('enter')
        print('Unblocked Enter Key')

def unblock_enter_after_delay(delay=2.0):
    """Calls unblock_enter after 2 seconds"""
    def delayed_unblock():
        unblock_enter()
    
    threading.Timer(delay, delayed_unblock).start()

def on_v(e):
    """If important information was just pasted, block enter key for 2 seconds"""
    # ctrl is not registered as a normal key so we must check it differently
    if keyboard.is_pressed('ctrl') and is_slack_active_window():
        detected, label, text = clipboard_has_secret()
        if detected:
            notifier.alert_secret_detected(label, text)
            block_enter_temporarily()
            unblock_enter_after_delay(delay=2.0)
        if config.get('clear_after_paste', False):

            delete_pasted_content()

def run_slack_guard():
    """Detects that user just tried to paste sensitive information and prevents them from hitting enter key"""
    keyboard.on_press_key("v", on_v, suppress=False)
    while True:
        time.sleep(1)