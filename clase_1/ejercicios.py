# Ejercicio 1
a = 2.4
b = -3.21
c = 47.8

print("a\tb\tc")
print(a,"\t", b, "\t", c)


# Ejercicio 3
palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese una palabra: ")
palabra3 = input("Ingrese una palabra: ")

longitud_palabra1 = "*"*len(palabra1)
# print(palabra1, longitud_palabra1)

longitud_palabra2 = "*"*len(palabra2)
# print(palabra2, longitud_palabra2)

longitud_palabra3 = "*"*len(palabra3)
# print(palabra3, longitud_palabra3)


# Ejercicio 4
diccionario_palabras = {
  palabra1: longitud_palabra1,
  palabra2: longitud_palabra2,
  palabra3: longitud_palabra3,
}

# print(diccionario_palabras)

for x in diccionario_palabras:
  print("llave:", x, "valor:", diccionario_palabras[x])