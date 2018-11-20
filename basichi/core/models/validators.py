# -*- encoding: utf8 -*-
from django.core.exceptions import ValidationError
from core.models.constants import (
    NOT_ZERO,
)

def valid_timedelta(timedelta, message=NOT_ZERO):
    # Retorna um objeto 
    # <django.core.exceptions.ValidationError> 
    # se o objeto recebido tiver valor `seconds` igual a zero.
    #  timedelta : <datetime.datetime.timedelta> requiered
    #  message : <string> not required. Default: NOT_ZERO

    if timedelta.seconds == 0:
        return ValidationError(message=message)
    return True

