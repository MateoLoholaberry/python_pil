""" Modelo de la clase Contacto:
    solo tiene 3 propiedades nombre, telefono, email
"""
class Contacto:
    def __init__(self, nombreCompleto, numero, email):
        self.nombre = nombreCompleto
        self.telefono = numero
        self.email = email
    
    
    