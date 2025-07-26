# src/tools.py

from notifier import send_email

def send_custom_email(recipient_email, subject, message):
    """
    Sends a custom email using the existing notifier.
    """
    return send_email(recipient_email, subject, message)
