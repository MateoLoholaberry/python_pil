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