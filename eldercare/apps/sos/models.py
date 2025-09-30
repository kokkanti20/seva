from django.db import models
from django.contrib.auth.models import User


class EmergencyContact(models.Model):
    CARRIERS = [
        ("att", "AT&T"),
        ("verizon", "Verizon"),
        ("tmobile", "T-Mobile"),
        ("sprint", "Sprint"),
        ("uscellular", "US Cellular"),
        ("googlefi", "Google Fi"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emergency_contacts")
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20, blank=True)
    carrier = models.CharField(max_length=50, choices=CARRIERS, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.phone or self.email})"


class SOSAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sos_alerts")
    message = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    delivered_to = models.TextField()  # comma-separated list of recipients
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SOS Alert from {self.user.username} at {self.created_at:%Y-%m-%d %H:%M}"
