import pystray
from PIL import Image, ImageDraw
from paste_with_peace.config import load_config
import sys
import subprocess

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
        exe_path = sys.executable
        subprocess.Popen([exe_path, "--settings"])

    def quit_action(icon, item):
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