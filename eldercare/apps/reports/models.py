from django.db import models
from django.contrib.auth.models import User

class HealthReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="health_reports")
    compliance_rate = models.FloatField(help_text="Medication adherence %")
    activity_summary = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Health Report for {self.user.username} on {self.generated_at.date()}"
