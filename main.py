from threading import Thread
from paste_with_peace.monitor import start_monitor
from paste_with_peace.tray import run_tray

if __name__ == "__main__":
    Thread(target=start_monitor, daemon=True).start()
    # Thread(target=run_tray, daemon=False).start()
    run_tray()