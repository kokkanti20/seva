from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MedicationViewSet, MedScheduleViewSet, MedEventViewSet

router = DefaultRouter()
router.register(r"meds", MedicationViewSet, basename="medication")
router.register(r"medschedules", MedScheduleViewSet, basename="medschedule")
router.register(r"medevents", MedEventViewSet, basename="medevent")

urlpatterns = [ path("", include(router.urls)) ]
