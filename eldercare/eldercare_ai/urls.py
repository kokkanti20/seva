from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthz/", lambda r: HttpResponse("OK")),
    path("api/", include("apps.meds.urls")),
    path("assistant/", include("apps.assistant.urls")),
    path("sos/", include("apps.sos.urls")),   # ✅ include sos urls
    path("reports/", include("apps.reports.urls")),
    path("", home, name="home"),              # ✅ homepage
]
