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