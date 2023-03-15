# Model imports
from contactoApp.models import Contacto


def contactoExiste(pk):
    try:
        contacto = Contacto.objects.get(pk=pk)
        return True, contacto
    except:
        contacto = 'El contacto no existe'
        return False, contacto