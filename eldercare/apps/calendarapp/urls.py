from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AppointmentViewSet, RoutineViewSet, AlertViewSet

router = DefaultRouter()
router.register(r"appointments", AppointmentViewSet, basename="appointment")
router.register(r"routines", RoutineViewSet, basename="routine")
router.register(r"alerts", AlertViewSet, basename="alert")

urlpatterns = [ path("", include(router.urls)) ]
