from django.db import models
from users.models import Patient, Dentist
from .procedure import Procedure

STATUS_CHOICES = {
    'agendada': 'Agendada',
    'concluída': 'Concluída',
    'cancelada': 'Cancelada',
}


class Appointment(models.Model):
    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    dentist = models.ForeignKey(
        Dentist, on_delete=models.CASCADE, verbose_name='Dentista')
    date = models.DateField(verbose_name='Agendada para')
    appointment_occasion = models.TextField(verbose_name='Motivo da Consulta')
    diagnosis = models.TextField(
        blank=True, null=True, verbose_name='Diagnóstico')
    procedures_done = models.ManyToManyField(
        Procedure, related_name='consultas', verbose_name='Procedimento(s)')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, verbose_name='Status')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Marcado em')

    def __str__(self) -> str:
        return f"Consulta de {self.patient} com {self.dentist} em {self.date}"
