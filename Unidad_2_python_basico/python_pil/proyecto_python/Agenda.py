import json
import pathlib
from Contacto import Contacto

""" Modelo de la clase Agenda
    tiene 1 propiedad: mis_contactos
    y tiene 8 métodos: hay_contactos - existe_contacto - agregar_contacto
    - mostrar_todos_contactos - mostrar_un_contacto - buscar_contactos
    - modificar_contacto - eliminar_contacto.
"""
class Agenda:
    def __init__(self):
        self.mis_contactos = []


    def hay_contactos(self):
        """ Retorna verdadero si la lista de "mis_contactos"
            no está vacia, sino retorna falso.
        """
        if len(self.mis_contactos) > 0:
            return True
        else:
            return False


    def existe_contacto(self, nombre):
        """ Verfica que exista el contacto en la lista.
            si existe lo devuelve, sino retorna falso.
        """
        for contacto in self.mis_contactos:
            if contacto.nombre == nombre:
                return contacto
        return False


    def agregar_contacto(self, nombre, telefono, email):
        """ Agrega contactos a la lista.
        """
        # Verifica que el telefono sea válido
        # Si no es válido ingresa un 0 en su lugar.
        if telefono.isdigit():
            telefono = telefono
        else:
            print("\nNo se ingresó un número válido.\nSe dejará por defecto un 0")
            telefono = 0

        nuevoContacto = Contacto(nombre, telefono, email)
        self.mis_contactos.append(nuevoContacto)
    
    
    def mostrar_todos_contactos(self):
        """ Muestra todos los contactos en la lista de mis_contactos.
        """
        for contacto in self.mis_contactos:
            self.mostrar_un_contacto(contacto)
    
    
    def mostrar_un_contacto(self, contacto):
        """ Muestra la información del contacto que se pasa por
            parametro.
        """
        print(f"Nombre: {contacto.nombre}")
        print(f"Telefono: {contacto.telefono}")
        print(f"E-Mail: {contacto.email}")
        print("^"*20)


    def buscar_contactos(self, nombre):
        """ Busca entre mis_contactos aquellos contactos
            que coincidan con el nombre pasado por parametro.
        """
        encontrados = 0
        for contacto in self.mis_contactos:
            if nombre in contacto.nombre:
                self.mostrar_un_contacto(contacto)
                encontrados += 1

        if encontrados == 0:
            print("No se encontró ningún contacto.")
        elif encontrados == 1:
            print("Se encontró 1 contacto")
        else:
            print(f"Se encontraron {encontrados} contactos")

    
    
    def modificar_contacto(self, contacto, nombre, telefono, email):
        """ Modifica un contacto especificado con los valores de nombre,
            telefono y email pasados por parámetros
        """
        # Verifica que el telefono sea válido
        # Si no es válido ingresa un 0 en su lugar.
        if telefono.isdigit():
            telefono = telefono
        else:
            print("\nNo se ingresó un número válido.\nSe dejará por defecto un 0")
            telefono = 0

        contacto.nombre = nombre
        contacto.telefono = telefono
        contacto.email = email


    def eliminar_contacto(self, contacto):
        """Elimina el contacto que se pasa por parámetro
        """
        self.mis_contactos.remove(contacto)
        print("Contacto eliminado con éxito.")

