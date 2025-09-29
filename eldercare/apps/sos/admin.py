from django.contrib import admin
from .models import SOSAlert

@admin.register(SOSAlert)
class SOSAlertAdmin(admin.ModelAdmin):
    list_display = ("triggered_by", "location", "timestamp", "resolved")
