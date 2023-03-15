"""
Aquí se encuentra la lógica del programa.
"""


from Agenda import Agenda
import os


def mostrar_menu():
    os.system('cls')
    print("""                        Agenda de contactos
1) Agregar contacto
2) Mostrar contactos
3) Buscar contacto
4) Modificar contacto
5) Eliminar contacto
0) Salir
""")

def main():
    continuar = True
    mi_agenda = Agenda()
    while continuar:
        mostrar_menu()
        opc = input("Selecciona una opción: ")

        if opc == "1":
            os.system("cls")
            print("                     Agregar contacto\n")
            nombre = input("Nombre y apellido: ")

            # Busca si existe el nombre del contacto en la agenda
            existe = mi_agenda.existe_contacto(nombre)

            # Si no existe entra y lo deja añadir
            if existe == False:
                telefono = input("Telefono: ")
                email = input("E-Mail: ")
                mi_agenda.agregar_contacto(nombre, telefono, email)
                print("\nEl contacto se agregó con éxito.")
            else:
                print("El contacto ya existe")

        elif opc == "2":
            os.system("cls")
            print("                     Mostrar contactos\n")

            # Si hay contactos en la agenda entra
            if mi_agenda.hay_contactos():
                # Muestra todos los contactos
                mi_agenda.mostrar_todos_contactos()
            else:
                print("No hay contactos registrados.")

        elif opc == "3":
            os.system("cls")
            print("                     Buscar contacto\n")
            
            # Si hay contactos en la agenda entra
            if mi_agenda.hay_contactos():
                nombre = input("nombre del contacto a buscar: ")
                print()

                # Busca y muestra todos los contactos que coincidan con el nombre
                mi_agenda.buscar_contactos(nombre)
            else:
                print("No hay contactos registrados.")

        elif opc == "4":
            os.system("cls")
            print("                     Modificar contacto\n")
            
            # Si hay contactos en la agenda entra
            if mi_agenda.hay_contactos():
                nombre = input("Nombre completo del contacto a modificar: ")
                
                # verifica que exista el contacto
                existe_contacto = mi_agenda.existe_contacto(nombre)
                
                # Entra si existe el contacto
                if existe_contacto != False:
                    print("\nInformación:")
                    # Muestra la información del contacto a modificar
                    mi_agenda.mostrar_un_contacto(existe_contacto)

                    # Le pide al usuario los nuevos datos del contacto.
                    print("Si desea conservar algún dato del contacto viejo presione enter.")
                    nuevo_nombre = input("Nuevo nombre: ") or existe_contacto.nombre
                    
                    telefono = input("Nuevo Telefono: ") or existe_contacto.telefono
                    
                    email = input("Nuevo E-Mail: ") or existe_contacto.email

                    # Modifica el contacto seleccionado
                    mi_agenda.modificar_contacto(existe_contacto, nuevo_nombre, telefono, email)
                    print("\nEl contacto se modificó con éxito.")
                else:
                    print("El contacto no existe")
            else:
                print("No hay contactos registrados.")

        elif opc == "5":
            os.system("cls")
            print("                     Eliminar contacto\n")
            
            # Si hay contactos en la agenda entra
            if mi_agenda.hay_contactos():
                nombre = input("Nombre: ")
                # Verifica que exista el contacto
                existe_contacto = mi_agenda.existe_contacto(nombre)
                
                # Entra si existe el contacto
                if existe_contacto != False:
                    # Elimina el contacto
                    mi_agenda.eliminar_contacto(existe_contacto)
                else:
                    print("El contacto no existe")
            else:
                print("No hay contactos registrados.")

        elif opc == "0":
            # Sale del While
            continuar = False
        else:
            print("\nOpción no válida.")

        input("\nPresiona enter para continuar...")
    print("\nFin del programa.")


if __name__ == "__main__":
    main()