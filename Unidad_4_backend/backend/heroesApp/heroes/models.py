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
        max_length=40,
        unique = True,
        verbose_name = 'Nombre'
    )
    
    age = models.IntegerField(
        verbose_name = 'Edad'
    )
    universe = models.CharField(
        max_length = 1,
        choices = UNIVERSE_CHOICES,
        verbose_name = 'Universo'
    )
    
    # Configura como se ven en el admin
    class Meta:
        verbose_name = 'Heroe'
        verbose_name_plural = 'Heroes'
    
    def __str__(self):
        return self.name