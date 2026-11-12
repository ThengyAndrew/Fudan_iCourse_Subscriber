"""Generate school authentication codes immediately before submission."""

import os

import pyotp


def school_totp() -> str:
    """Return the current code without logging the code or its secret."""
    secret = os.environ.get("SCHOOL_TOTP_SECRET", "").strip().replace(" ", "")
    if not secret:
        raise RuntimeError("SCHOOL_TOTP_SECRET is not configured")
    return pyotp.TOTP(secret).now()
