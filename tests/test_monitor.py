from paste_with_peace import monitor

# we don't actually want to see alerts when we run tests so we need 
# to make a notifier that gives results in a different way
class MockNotifier:
    def __init__(self):
        self.called = False
        self.label = None
        self.text = None
    
    def alert_secret_detected(self, label, text):
        self.called = True
        self.label = label
        self.text = text

def test_detect_secret(monkeypatch):
    mock = MockNotifier()
    # use monkeypatch to run tests with MockNotifier
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    
    result = monitor.scan_clipboard_text("sk-abcdef1234567890abcdef1234567890")
    assert result is True
    assert mock.called
    assert "OpenAI" in mock.label

def test_detect_aws_access_key(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("AKIA1234567890ABCD12")
    assert result is True
    assert mock.called
    assert "AWS Access Key" in mock.label

def test_detect_aws_secret_key(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("aws secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")
    assert result is True
    assert mock.called
    assert "AWS Secret Key" in mock.label

def test_detect_google_api_key(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("AIzaSyA-abcdefghijklmnopqrstuvwxyz1234567890_")
    assert result is True
    assert mock.called
    assert "Google API Key" in mock.label

def test_detect_slack_token(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("xoxb-123456789012-123456789012-abcdefghijklmnopqrstu")
    assert result is True
    assert mock.called
    assert "Slack Token" in mock.label

def test_detect_github_token(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("ghp_abcdefghijklmnopqrstuvwxyzABCDEF1234567890")
    assert result is True
    assert mock.called
    assert "GitHub Token" in mock.label

def test_detect_heroku_api_key(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("heroku key: 0123456789abcdef0123456789abcdef")
    assert result is True
    assert mock.called
    assert "Heroku API Key" in mock.label

def test_detect_stripe_secret_key(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("sk_live_1234567890abcdefghijklmnopqrstuvwxyz")
    assert result is True
    assert mock.called
    assert "Stripe Secret Key" in mock.label

def test_detect_stripe_publishable_key(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("pk_live_1234567890abcdefghijklmnopqrstuvwxyz")
    assert result is True
    assert mock.called
    assert "Stripe Publishable Key" in mock.label

def test_detect_twilio_api_key(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("SK0123456789abcdef0123456789abcdef")
    assert result is True
    assert mock.called
    assert "Twilio API Key" in mock.label

def test_detect_sendgrid_api_key(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("SG.abcdEFGHijklmnopQRSTuv.1234567890abcdefGHIJKLMNOPQRSTuvwxYZ1234567890XYZ")
    assert result is True
    assert mock.called
    assert "SendGrid API Key" in mock.label

def test_detect_generic_api_key(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)
    result = monitor.scan_clipboard_text("api_key: abc349058defghijklmnop")
    assert result is True
    assert mock.called
    assert "Generic API Key" in mock.label

def test_ignore_safe(monkeypatch):
    mock = MockNotifier()
    monkeypatch.setattr("paste_with_peace.notifier.alert_secret_detected", mock.alert_secret_detected)

    result = monitor.scan_clipboard_text("hello world this is normal text and definitely doesn't have anything confidential")
    assert result is False
    assert mock.called is False