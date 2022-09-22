# Clases
class Animal:

    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self, sonido):
        print(sonido)


class Perro(Animal):

    # Atributos de clase == globales
    # especie = "mamiferos"

    def __init__(self, nombre, raza, especie, edad):
        # Atributos de instancia == locales
        self.nombre = nombre
        self.raza = raza
        super().__init__(especie, edad)

    # Métodos
    # def ladrar(self):
    #     print("guauu guauu")


    def jugar(self, objeto):
        print(f"{self.nombre} está jugando con {objeto}")


    def saludar(self):
        print(f"{self.nombre} te dió la pata")


class Gato(Animal):

    # Atributos de clase == globales
    # especie = "mamiferos"

    def __init__(self, nombre, raza, especie, edad):
        # Atributos de instancia == locales
        self.nombre = nombre
        self.raza = raza

        super().__init__(especie, edad)

    # Métodos
    # def ladrar(self):
    #     print("guauu guauu")


    def jugar(self, objeto):
        print(f"{self.nombre} está jugando con {objeto}")


    def saludar(self):
        print(f"{self.nombre} ronronea")



perro_1 = Perro("Renato", "calle", "canino", 5)
print(f"perro_1 -> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}")
perro_1.saludar()


# gato_1 = Gato("Tito", "Cálico", "Felino", 3)
# print(f"gato_1 -> {gato_1.nombre}, {gato_1.raza}, {gato_1.especie}")
# gato_1.saludar()
