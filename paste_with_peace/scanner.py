import re
import math
from typing import Tuple

def calculate_entropy(s: str) -> float:
    """Calculate Shannon entropy of a string.
    For more info, see: https://en.wikipedia.org/wiki/Entropy_(information_theory)"""
    prob = [float(s.count(c)) / len(s) for c in set(s)]
    # Calculate sum of multiplying each prob p(c) by log2 of 
    # itself for each char c
    return -sum([p * math.log2(p) for p in prob])

def is_potential_secret(text: str) -> Tuple[bool, str]:
    """Check if the string likely contains a secret.
    DISCLAIMER: Not tested to a level that guarantees security.
    This tool is meant to supplment other security tools that are 
    already in place."""
    # For any individual company, this should be customized to keys that
    # match services used by the company
    patterns = {
        "AWS Access Key": r"AKIA[0-9A-Z]{16}",
        "AWS Secret Key": r"(?i)aws(.{0,20})?(secret|key)[\s:=\"']+[A-Za-z0-9/+=]{40}",
        "OpenAI Key": r"sk-[A-Za-z0-9]{32,}",
        "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
        "Slack Token": r"xox[baprs]-[0-9a-zA-Z]{10,48}",
        "GitHub Token": r"gh[pousr]_[A-Za-z0-9_]{36,255}",
        "Heroku API Key": r"(?i)heroku(.{0,20})?key[\s:=\"']+[0-9a-fA-F]{32}",
        "Stripe Secret Key": r"sk_live_[0-9a-zA-Z]{24}",
        "Stripe Publishable Key": r"pk_live_[0-9a-zA-Z]{24}",
        "Twilio API Key": r"SK[0-9a-fA-F]{32}",
        "SendGrid API Key": r"SG\.[A-Za-z0-9_\-\.]{22}\.[A-Za-z0-9_\-\.]{43}",
        "Generic API Key": r"(?i)(api|secret|token|password)\w*[\s:=\"']+[^\s]{12,}"
    }

    for label, pattern in patterns.items():
        if re.search(pattern, text):
            return True, label

    # Fallback: entropy check
    if len(text) > 20 and calculate_entropy(text) > 4.5:
        return True, "No pattern match, but High Shannon Entropy found"

    return False, ""