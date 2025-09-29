from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    doctor_name = models.CharField(max_length=120, blank=True)
    hospital = models.CharField(max_length=200, blank=True)
    start_ts = models.DateTimeField()
    end_ts = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=240, blank=True)  # free text address
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.doctor_name} @ {self.hospital} on {self.start_ts.date()}"


class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="routines")
    type = models.CharField(
        max_length=32,
        choices=[
            ("meal", "Meal"),
            ("walk", "Walk"),
            ("hydration", "Hydration"),
            ("sleep", "Sleep"),
        ],
    )
    recurrence = models.CharField(max_length=64, default="daily")
    target = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.type} ({self.recurrence})"


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alerts")
    type = models.CharField(max_length=32)
    severity = models.CharField(max_length=16, default="info")
    message = models.TextField()
    acknowledged_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="acknowledged_alerts"
    )
    ack_ts = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.severity}] {self.type}: {self.message[:30]}"
