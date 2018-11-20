# -*- encoding utf-8 -*-

from logging import Logger
from core.models.constants import (
    AP_CONFLICT
)

class AppointmentConflictError(Exception):
    """
    Erro específico para
    <core.models.main.Appointment>
    Ocorre quando há conflitos entre agendamentos de programas
    """
    def __init__(self, arguments):
        Exception.__init__(self, AP_CONFLICT.format(arguments))
        self.arguments = arguments

