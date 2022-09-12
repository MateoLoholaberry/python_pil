# Idear un programa que solicite al usuario dos números enteros y el programa
# deberá retornar aquellos números pares que se encuentren dentro del rango
# formado entre los números ingresados.

entero_1 = int(input("Ingrese el primer número: "))

entero_2 = int(input("Ingrese el segundo número: "))

print("Los números pares del rango son:")
if entero_1 > entero_2:
    for x in range(entero_2, entero_1+1):
        if x % 2 == 0:
            print(x)
else:
    for x in range(entero_1, entero_2+1):
        if x % 2 == 0:
            print(x)