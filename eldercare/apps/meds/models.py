from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    before_food = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.dosage})"


class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medications")
    name = models.CharField(max_length=120)
    strength = models.CharField(max_length=64, blank=True)
    unit = models.CharField(max_length=32, blank=True)
    instructions = models.TextField(blank=True)  # e.g., before/after food
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

class MedSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="med_schedules")
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name="schedules")
    dose = models.CharField(max_length=32, help_text="e.g., 1 pill")
    times_json = models.JSONField(default=list)  # ["08:00","20:00"]
    safe_window_min = models.IntegerField(default=60)
    safe_window_max = models.IntegerField(default=180)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

class MedEvent(models.Model):
    schedule = models.ForeignKey(MedSchedule, on_delete=models.CASCADE, related_name="events")
    due_at = models.DateTimeField()
    status = models.CharField(max_length=16, choices=[
        ("pending","pending"),("taken","taken"),("missed","missed"),("skipped","skipped")
    ], default="pending")
    taken_at = models.DateTimeField(null=True, blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
