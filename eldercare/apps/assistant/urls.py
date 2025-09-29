from django.urls import path
from .views import parse_med, weekly_summary

urlpatterns = [
    path("parse_med/", parse_med),
    path("weekly_summary/<int:user_id>/", weekly_summary),
]
