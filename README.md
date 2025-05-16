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