from django.contrib import admin

# Register your models here.
from core.models import (
    Program,
    Appointment
)

admin.site.register(Program)
admin.site.register(Appointment)
