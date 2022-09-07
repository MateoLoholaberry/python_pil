# Condicionales en Python
# If-Else
"""
a = 1
b = 2
c = 5

if a > b:
    if a > c:
        print("A es el mayor:", a)
    else:
        print("C es el mayor", c)
else:
    if b > c:
        print("B es el mayor:", b)
    else:
        print("C es el mayor:", c)


print("final")

"""


from re import S


edad_juan = 16

if edad_juan >= 16 and edad_juan >= 18:
    print("Juan puede votar y es mayor de edad")
else:
    print("No cumple con alguna de las condiciones")


# Elif
a = 5

if a == 3:
    print("A es igual a 3")
elif a == 4:
    print("A es igual a 4")
elif a == 5:
    print("A es igual a 5")



