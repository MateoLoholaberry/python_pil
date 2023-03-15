from django.db import models


# Create your models here.
class Hero(models.Model):

    # Opciones
    UNIVERSE_CHOICES = (
        ('1', 'Marvel'),
        ('2', 'DC')
    )

    # Atributos
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nombre'
    )

    secret_identity = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Identidad secreta'
    )

    age = models.IntegerField(
        null=True,
        verbose_name='Edad'
    )

    universe = models.CharField(
        max_length=1,
        choices=UNIVERSE_CHOICES,
        verbose_name='Universo'
    )

    class Meta:
        verbose_name = 'Heroe'
        verbose_name_plural = 'Heroes'
