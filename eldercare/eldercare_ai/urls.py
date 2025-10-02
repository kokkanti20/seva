from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# import views from assistant app (correct location)
from apps.assistant.views_voice import voice_assistant, tts_demo


def home(request):
    return render(request, "home.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthz/", lambda r: HttpResponse("OK")),
    path("api/", include("apps.meds.urls")),
    path("assistant/voice/", voice_assistant, name="voice_assistant"),
    path("assistant/tts-demo/", tts_demo, name="tts_demo"),
    path("sos/", include("apps.sos.urls")),
    path("reports/", include("apps.reports.urls")),
    path("calendar/", include("apps.calendarapp.urls")),  # ✅ calendar route
    path("", home, name="home"),
]
