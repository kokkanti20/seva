from rest_framework import viewsets, permissions
from .models import Appointment, Routine, Alert
from .serializers import AppointmentSerializer, RoutineSerializer, AlertSerializer

class BaseOwnedViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AppointmentViewSet(BaseOwnedViewSet):
    serializer_class = AppointmentSerializer
    model = Appointment
    queryset = Appointment.objects.all()

class RoutineViewSet(BaseOwnedViewSet):
    serializer_class = RoutineSerializer
    model = Routine
    queryset = Routine.objects.all()

class AlertViewSet(BaseOwnedViewSet):
    serializer_class = AlertSerializer
    model = Alert
    queryset = Alert.objects.all()
