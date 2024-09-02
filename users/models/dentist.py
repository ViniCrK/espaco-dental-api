from django.db import models

SPECIALTY_CHOICES = {
    'endodontia': 'Endodontia',
    'estomatologia': 'Estomatologia',
    'ortodontia': 'Ortodontia',
    'periodontia': 'Periodontia',
    'odontopediatria': 'Odontopediatria',
}


class Dentist(models.Model):
    class Meta:
        verbose_name = 'Dentista'
        verbose_name_plural = 'Dentistas'

    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    cro = models.CharField(max_length=20, unique=True, verbose_name='CRO')
    specialty = models.CharField(
        max_length=20, choices=SPECIALTY_CHOICES, verbose_name='Especialidade')
    phone = models.CharField(max_length=15, verbose_name='Telefone')

    def __str__(self) -> str:
        return f'{self.name} - {self.specialty}'
