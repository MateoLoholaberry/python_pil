# Models imports
from heroes.models import Hero

def hayHeroe(pk):
    
    try:
        heroe = Hero.objects.get(pk=pk)
        return True, heroe

    except:
        heroe = {
            'mensaje':'El heroe que se pasó por parametró no existe...'
        }
        return False, heroe