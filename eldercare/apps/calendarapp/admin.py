from django.contrib import admin
from .models import Appointment, Routine, Alert

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("doctor_name", "hospital", "start_ts", "end_ts", "location")

@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ("user", "type", "recurrence", "target")

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ("user", "type", "severity", "created_at", "ack_ts")
