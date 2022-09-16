# Clases

class Perro:

    # Atributos de clase == globales
    especie = "mamiferos"

    def __init__(self, nombre, raza):
        # Atributos de instancia == locales
        self.nombre = nombre
        self.raza = raza


    # Métodos
    def ladrar(self):
        print("guauu guauu")


    def jugar(self, objeto):
        print(f"{self.nombre} está jugando con {objeto}")


    def saludar(self):
        print("Guau, mi nombre es", self.nombre)



perro_1 = Perro("Renato", "calle")
print(f"perro_1 -> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}")
perro_1.jugar("hueso")
perro_1.ladrar()
perro_1.saludar()


perro_2 = Perro("Lila", "Collie")
print(f"Perro_2 -> {perro_2.nombre}, {perro_2.raza}, {perro_2.especie}")
perro_2.saludar()


