from django.db import models


class Procedure(models.Model):
    class Meta:
        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'

    name = models.CharField(max_length=255, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    cost = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Custo')

    def __str__(self) -> str:
        return f'{self.name}'
