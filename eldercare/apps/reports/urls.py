from django.urls import path
from .views import demo_report_text
urlpatterns = [ path("weekly/<int:user_id>/", demo_report_text) ]
