# a = "Esto es una cadena"
# b = "Esto es otra cadena"


# print(a, type(a))
# print(b, type(b))

# c = str(120.56)
# print(c, type(c))


# print(len(a))
# print(a[0:4])
# print(a.lower())
# print(a.upper())


lista_1 = ["Hola", 4, True, 2.5, [1,2,3,4], ("a", "b")]
print(lista_1)

print(type(lista_1))
print(len(lista_1))
print(lista_1[3])

var_uno = lista_1[2]
print(var_uno)


# Diccionarios

usuario = {
  "nombre": "Octavio",
  "apellido": "Gomez",
  "edad": 38,
  "hobbies": ["futbol", "música"],
  "mascotas": False,
}


print(usuario)
print(usuario["nombre"])
print(usuario["edad"])

print(usuario.get("hobbies", "no encontrado"))
print(usuario.get("puesto", "no encontrado"))


keys_usuario = list(usuario.keys())
print(type(keys_usuario))
print(usuario.get(keys_usuario[0]))
