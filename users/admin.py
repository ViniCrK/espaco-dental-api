from django.contrib import admin
from users import models


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('id',)


@admin.register(models.Dentist)
class DentistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialty', )
    ordering = ('id',)
