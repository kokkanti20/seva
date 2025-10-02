from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthz/", lambda r: HttpResponse("OK")),
    path("api/", include("apps.meds.urls")),
    path("assistant/", include("apps.assistant.urls")),  # ✅ your local voice endpoints
    path("sos/", include("apps.sos.urls")),
    path("reports/", include("apps.reports.urls")),
    path("", home, name="home"),
]

# Serve media (for generated audio files, etc.)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
