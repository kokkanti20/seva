from django.contrib import admin
from .models import EmergencyContact, SOSAlert

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "carrier", "email", "user")
    search_fields = ("name", "phone", "email", "user__username")

@admin.register(SOSAlert)
class SOSAlertAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "created_at", "delivered_to")
