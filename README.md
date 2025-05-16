# paste-with-peace

### Features (MVP)
- ✅ Detects potential secrets using pattern matching and entropy scoring:
  - AWS Keys (AKIA...)
  - OpenAI API Keys (sk-...)
  - Generic secret-looking variables

### Features (MVP)
- ✅ Clipboard monitor that checks for copied secrets in real time
- ✅ Uses `scanner.py` to detect and `notifier.py` to alert
- ✅ Tested with unit tests and mock notifier

- ✅ Desktop notification includes type and recommended action

### Logging

Detected secrets are logged to `detection_log.txt` with:
- Timestamp
- Type of secret (e.g., AWS Key, OpenAI Key)
- A truncated preview (first 40 characters)

### Configuration

You can customize the app with `config.json` in the root directory.

Example:
```json
{
  "logging_enabled": true,
  "log_file_path": "detection_log.txt",
  "popup_timeout": 6
}
```

### Tray Options

The tray icon shows system status and optional actions.

To disable the ability for users to quit the monitor:
```json
"allow_user_quit": false
```

### Installation

You can run Paste with Peace by double-clicking the `PasteWithPeace.exe` file.

No Python installation required.

To configure options, edit the `config.json` in the same folder.

### 🧽 Auto-Delete Pasted Secret (Slack)

When you paste a secret into the Slack Desktop app using `Ctrl+V`, Paste with Peace can automatically delete just the pasted portion from the input field.

#### Behavior:
- Scans the clipboard after `Ctrl+V` in Slack
- If a secret is detected:
  - Shows a desktop warning
  - Blocks the `Enter` key for 2 seconds
  - Deletes only the pasted content by simulating `Backspace` presses

#### Configurable in `config.json`:
```json
"clear_after_paste": true
```

### 🛠 Settings UI

Paste with Peace includes a modern graphical interface for editing your configuration.

To launch the UI:

```bash
python -m paste_with_peace.settings_ui
```