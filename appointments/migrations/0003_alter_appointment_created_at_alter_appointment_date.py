# Generated by Django 5.1.1 on 2024-09-17 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(verbose_name='Marcada para'),
        ),
    ]
