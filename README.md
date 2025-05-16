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