# Default email (console for now)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "sos@eldercare.ai"

# SMS gateways (email-to-SMS free carriers)
SMS_GATEWAYS = {
    "verizon": "vtext.com",
    "att": "txt.att.net",
    "tmobile": "tmomail.net",
}
