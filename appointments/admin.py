from django.contrib import admin
from appointments import models


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'dentist',
                    'date', 'status', 'created_at', )
    ordering = ('date', )


@admin.register(models.Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', )
    ordering = ('id', )
