from django.db import models

# Create your models here.

class Usuario (models.Model):
    """modelo de un usuario
    """

    #Atributos
    nombre = models.CharField(
        max_length=40,
        verbose_name = 'Nombre'
    )

    apellido = models.CharField(
        max_length=40,
        verbose_name='Apellido'
    )

    user_name = models.CharField(
        max_length=40,
        unique = True,
        verbose_name='User name'
    )

    contrasenia = models.CharField(
        max_length=255,
        verbose_name='Contraseña'
    )


    # Configuración
    class Meta:
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'

    def __str__(self):
        return self.nombre + " " + self.apellido