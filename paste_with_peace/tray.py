import pystray
from PIL import Image, ImageDraw
from paste_with_peace.config import load_config, get_config_path
import sys
import subprocess
import os

# placeholder for the system tray icon. will be replaced with custom
# pixel art later
def create_icon():
    """Create a simple red circular icon in memory."""
    image = Image.new("RGB", (64, 64), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((16, 16, 48, 48), fill="red")
    return image

def run_tray(on_quit_callback=None):
    """Shows icon in the tray. Includes a Settings launcher and optional Quit."""

    config = load_config()  # <-- Always load fresh config when tray starts

    def open_settings_gui(icon, item):
        env = os.environ.copy()
        env["PWP_SETTINGS"] = "1"
        if getattr(sys, 'frozen', False):
            # Running as exe
            exe_path = sys.executable
            subprocess.Popen([exe_path], env=env)
        else:
            # Running from source
            subprocess.Popen([sys.executable, os.path.abspath("main.py")], env=env)

    def quit_action(icon, item):
        # Signal settings UI to quit
        flag_path = os.path.join(os.path.dirname(get_config_path()), "quit.flag")
        with open(flag_path, "w") as f:
            f.write("quit")
        icon.stop()
        if on_quit_callback:
            on_quit_callback()
        sys.exit(0)

    menu_items = [
        pystray.MenuItem("Settings", open_settings_gui)
    ]

    if config.get("allow_user_quit", False):
        menu_items.append(pystray.MenuItem("Quit", quit_action))

    icon = pystray.Icon("Paste with Peace")
    icon.icon = create_icon()
    icon.menu = pystray.Menu(*menu_items)
    icon.run()