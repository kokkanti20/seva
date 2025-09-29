from django.contrib import admin
from .models import HealthReport

@admin.register(HealthReport)
class HealthReportAdmin(admin.ModelAdmin):
    list_display = ("user", "compliance_rate", "generated_at")
