from threading import Thread
from paste_with_peace.monitor.monitor import start_monitor
from paste_with_peace.tray import run_tray
from paste_with_peace.intercept.slack_guard import run_slack_guard

if __name__ == "__main__":
    Thread(target=start_monitor, daemon=True).start()
    Thread(target=run_slack_guard, daemon=True).start()
    run_tray()

    # I think the next feature should be that when a user learns their enter key is blocked, they can click a button somewhere that redacts the sensitive information. therefore let's first build the ability to redact the sensitive information, but let's not make it run automatically