from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import (
    Program,
    Appointment
)
from core.serializers import (
    ProgramSerializer,
    AppointmentSerializer
)
from core.models.utils import(
    create_or_update_dict
)
from datetime import datetime, timedelta

#/calendar/day
@api_view(['GET'])
def get_calendar(request, day):
    """
    Getting the calender of the day
    """
    try:
        day = datetime.strptime("%Y-%m-%d")
    except ValueError:
        day = datetime.today()
    start = {
        "hour": 0,
        "minute": 0,
        "second": 0
    }
    end = {
        "hour": 23,
        "minute": 59,
        "second": 59
    }
    day_start = day.replace(**start)
    day_end = day.replace(**end)

    all_programs = Program.objects.filter(
        appointments__date_start__gt=day_start,
        appointments__date_end__lt=day_end,
        ).order_by("-appointments__date_start")

    serialized_response = AppointmentSerializer(all_programs).data
    return Response(serialized_response)

    



    