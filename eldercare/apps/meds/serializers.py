from rest_framework import serializers
from .models import Medication, MedSchedule, MedEvent

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"

class MedScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedSchedule
        fields = "__all__"

class MedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedEvent
        fields = "__all__"
