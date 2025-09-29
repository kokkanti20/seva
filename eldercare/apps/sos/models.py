from django.db import models

class SOSAlert(models.Model):
    triggered_by = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"SOS by {self.triggered_by} at {self.timestamp}"
