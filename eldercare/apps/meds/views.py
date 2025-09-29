from rest_framework import viewsets, permissions
from .models import Medication, MedSchedule, MedEvent
from .serializers import MedicationSerializer, MedScheduleSerializer, MedEventSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return getattr(obj, "user_id", None) == request.user.id or getattr(getattr(obj, "medication", None), "user_id", None) == request.user.id

class MedicationViewSet(viewsets.ModelViewSet):
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Medication.objects.all()

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MedScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = MedScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = MedSchedule.objects.all()

    def get_queryset(self):
        return MedSchedule.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MedEventViewSet(viewsets.ModelViewSet):
    serializer_class = MedEventSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = MedEvent.objects.select_related("schedule","schedule__medication")

    def get_queryset(self):
        return MedEvent.objects.filter(schedule__user=self.request.user)
