import os
from celery import Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE","eldercare_ai.settings")
app = Celery("eldercare_ai")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
