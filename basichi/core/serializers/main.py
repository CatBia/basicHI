from rest_framework.serializers import (
    ModelSerializer)
from core.models import (
    Program,
    Appointment
)

class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = (
            "name",
            "description",
            "duration")

class AppointmentSerializer(ModelSerializer):
    model = Appointment
    fields = (
        "time"
    )