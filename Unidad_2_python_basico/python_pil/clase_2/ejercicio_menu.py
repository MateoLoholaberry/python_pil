# Realizar un menú de un cajero automático, donde el usuario pueda escoger entre
# alguna de las siguientes opciones:
# Deposito.
# Extracción.
# Transferencia.
# Salir.
# En todos los casos se le pedirá al usuario ingresar un monto de dinero y el
# programa deberá mostrar en todo momento la sección del menú en la que se
# encuentre, pudiendo retornar al menú principal siempre que se quiera y solo se
# detendrá la ejecución cuando se ingrese la opción de “salir” en el menú principal.

bandera = True

while bandera:
    print("""
Seleccione alguna de las siguientes opciones:
1) Deposito
2) Extracción
3) Transferencia
4) Salir
""")

    respuesta = input("Ingrese su opción: ")
    
    if respuesta == "1":
        print("                         Sección Depósito")
        monto = input("Ingrese un monto a depositar: ")
    elif respuesta == "2":
        print("                         Sección Extracción")
        monto = input("Ingrese un monto a depositar: ")
    elif respuesta == "3":
        print("                         Sección Transferencia")
        monto = input("Ingrese un monto a depositar: ")
    elif respuesta == "4":
        print("Hasta luego!")
        bandera = False
    else:
        print("No seleccionó una opción válida")
        input("Presione enter para continuar...")