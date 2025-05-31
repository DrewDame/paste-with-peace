import sys
import os
import time
from threading import Thread
from paste_with_peace.config import load_config, get_config_path
from paste_with_peace.monitor.monitor import start_monitor
from paste_with_peace.tray import run_tray
from paste_with_peace.intercept.slack_guard import run_slack_guard
from paste_with_peace import settings_ui

def monitor_restart_flag():
    print("monitor_restart_flag running")
    flag_path = os.path.join(os.path.dirname(get_config_path()), "restart.flag")
    while True:
        if os.path.exists(flag_path):
            os.remove(flag_path)
            os._exit(0)  # Immediately terminate the process and all threads
        time.sleep(1)

if __name__ == "__main__":
    # Wait for any previous instance to remove the restart flag
    flag_path = os.path.join(os.path.dirname(get_config_path()), "restart.flag")
    while os.path.exists(flag_path):
        time.sleep(0.1)

    # Start the restart flag monitor in the background
    Thread(target=monitor_restart_flag, daemon=True).start()

    # If launched with the settings environment variable, open only the settings GUI
    if os.environ.get("PWP_SETTINGS") == "1":
        settings_ui.SettingsApp().mainloop()
    else:
        config = load_config()
        enabled_apps = config.get("enabled_apps", {})

        Thread(target=start_monitor, daemon=True).start()

        if enabled_apps.get("slack", True):
            Thread(target=run_slack_guard, daemon=True).start()
        
        run_tray()