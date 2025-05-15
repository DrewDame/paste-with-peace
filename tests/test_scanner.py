from paste_with_peace import scanner

def test_aws_access_key():
    assert scanner.is_potential_secret("AKIA123456XY7890ABCD") == (True, "AWS Access Key")

def test_aws_secret_key():
    assert scanner.is_potential_secret("aws secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY") == (True, "AWS Secret Key")

def test_openai_key():
    assert scanner.is_potential_secret("sk-abcdefghijklmnopqrstuvwxyzABCDEF1234567890") == (True, "OpenAI Key")

def test_google_api_key():
    assert scanner.is_potential_secret("AIzaSyA-abcdefghijklmnopqrstuvwxyz1234567890_") == (True, "Google API Key")

def test_slack_token():
    assert scanner.is_potential_secret("xoxb-123456789012-123456789012-abcdefghijklmnopqrstu") == (True, "Slack Token")

def test_github_token():
    assert scanner.is_potential_secret("ghp_abcdefghijklmnopqrstuvwxyzABCDEF1234567890") == (True, "GitHub Token")

def test_heroku_api_key():
    assert scanner.is_potential_secret("heroku key: 0123456789abcdef0123456789abcdef") == (True, "Heroku API Key")

def test_stripe_secret_key():
    assert scanner.is_potential_secret("sk_live_1234567890abcdefghijklmnopqrstuvwxyz") == (True, "Stripe Secret Key")

def test_stripe_publishable_key():
    assert scanner.is_potential_secret("pk_live_1234567890abcdefghijklmnopqrstuvwxyz") == (True, "Stripe Publishable Key")

def test_twilio_api_key():
    assert scanner.is_potential_secret("SK0123456789abcdef0123456789abcdef") == (True, "Twilio API Key")

def test_sendgrid_api_key():
    assert scanner.is_potential_secret("SG.abcdEFGHijklmnopQRSTuv.1234567890abcdefGHIJKLMNOPQRSTuvwxYZ1234567890XYZ") == (True, "SendGrid API Key")

def test_generic_api_key():
    assert scanner.is_potential_secret("api_key: abc349058defghijklmnop") == (True, "Generic API Key")


def test_high_entropy_no_pattern():
    # This string is random, long, and does not match any pattern, but has high entropy
    high_entropy = "a8Fj3kLm9Qw2Zx7Vb6Np4Tg1Hs5Yc0Ur"
    # Ensure entropy is above 4.5 for this string
    assert scanner.calculate_entropy(high_entropy) > 4.5
    assert scanner.is_potential_secret(high_entropy) == (True, "No pattern match, but High Shannon Entropy found")

def test_safe_text():
    assert scanner.is_potential_secret("hello world, nothing to see here!") == (False, "")