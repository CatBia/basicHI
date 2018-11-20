# -*- encoding utf-8 -*-
#   Este arquivo e o model principal
#   aonde estao as funcoes mais basicas
#   do projeto
#

from django.utils.translation import gettext as _
from recurrence.fields import RecurrenceField
from recurrence import (
    WEEKLY,
    Rule,
    Recurrence
)
from datetime import (
    datetime,
    timedelta
)
from django.db.models import (
    Model,
    CharField,
    EmailField,
    TimeField,
    IntegerField,
    TextField,
    DurationField,
    ForeignKey,
    OneToOneField,
    DateTimeField,
    CASCADE,
    SET_NULL
)
from core.models.constants import (
    NO_EMPTY_EDIT_UFIELD,
    NO_EMPTY_FIELD,
    EMPTY_FIELD,
    MAX_OCCURRENCES,
    MAX_RECURRENCE_DAYS,
    FUTEBOL,
    NOVELA,
    MUSICAL,
    ENTREVISTAS,
    TYPE_CHOICES,
    PRINCIPAL
)
from core.models.validators import (
    valid_timedelta,
)
from core.models.constants import (
    AP_CONFLICT
)
from core.models.utils import (
    AppointmentConflictError
)
        

class Appointment(Model):
    date_start= DateTimeField(
        verbose_name="Start",
        **NO_EMPTY_FIELD
    )
    date_end= DateTimeField(
        verbose_name="End",
        **NO_EMPTY_FIELD
    )
    def get_conflict(self, *args):
        has_conflict = cls.objects.filter(
            date_start__gt=self.date_start,
            date_end__lt=self.date_end)
        if category:
            has_conflict.filter(program_set__category=category)
        if has_conflict:
            return has_conflict
        return False


class Program(Model):
    name = CharField(
        name = "name",
        max_length = 100,
        help_text = _("The name fo the program"),
        **NO_EMPTY_EDIT_UFIELD)
    description = TextField(
    )
    appointments = ForeignKey(
        Appointment,
        on_delete=CASCADE
    )
    category = CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        **NO_EMPTY_FIELD
    )        

        
    