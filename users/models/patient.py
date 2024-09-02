from django.db import models

GENDER_CHOICES = {
    'f': 'Feminino',
    'm': 'Masculino',
    'outro': 'Outro',
}


class Patient(models.Model):
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    gender = models.CharField(
        max_length=5, choices=GENDER_CHOICES, verbose_name='Gênero')
    phone = models.CharField(max_length=15, verbose_name='Telefone')

    def __str__(self) -> str:
        return f'{self.name}'
