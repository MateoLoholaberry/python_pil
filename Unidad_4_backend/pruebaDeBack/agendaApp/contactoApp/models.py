from django.db import models

# Create your models here.
class Contacto(models.Model):


    # Atributos
    name = models.CharField(
        max_length = 40,
        verbose_name = 'Nombre'
    )
    
    lastName = models.CharField(
        max_length = 40,
        verbose_name = 'Apellido'
    )
    
    phone = models.CharField(
        max_length = 20,
        verbose_name = 'Telefono'
    )
    
    def __str__(self):
        return f'{self.name} {self.lastName}'