# Nommbre
# Argumentos
# Código
# Retorno

def sumar(a,b):
  
  resultado = a+b
  
  return resultado


print(sumar(2,3))


# Función 2
def resta():
  resultado = 2-3
  
  return resultado

print(resta())


# Función 3

# def resta_2():
#   print(2-3)

# resta_2()


def saludo(cantidad_saludos):
  """
  Función que recoge los nombres ingresados por el usuario y los devuelve en una lista.
  """

  lista_nombres = []

  # Bucle de ingreso de nombres
  for i in range(cantidad_saludos):
    nombre = input("Ingrese su nombre: ")
    print("Hola", nombre)

    lista_nombres.append(nombre)

  # print(lista_nombres)
  return lista_nombres


nombres = saludo(int(input("Ingrese la cantidad de saludos: ")))

def orden(lista, sentido):
  """Esta función nos permite ordenar una lista en base a un sentido determinado

  Args:
      lista (list): Lista generica
      sentido (bool): Definir si la lista se ordena de forma ascendente o descendente

  Returns:
      list: lista ordenada
  """

  lista.sort(reverse=sentido)

  return lista


print(orden(nombres, True))




"""
def prueba(a,b,c):
  print(a,b,c)


a = 420
b = 3
c = 5

prueba(b=b, c=c, a=a) """

