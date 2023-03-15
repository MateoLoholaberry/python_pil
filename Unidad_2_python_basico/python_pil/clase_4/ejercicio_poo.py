# Crear una clase padre y clases hijas de personajes buenos y malos y poder hacerlos atacarse entre ellos

""" Ejercicio realizado durante la clase.
    todavía no está terminado, falta implementar algunos métodos
    al main como los de curarse. A la vez le falta trabajar más
    el main para que sea un programa un poco más complejo.
"""
import random
import os


class Personajes:
    def __init__(self, vida, nombre, vendas, balas):
        self.vida = vida
        self.nombre = nombre
        self.vendas = vendas
        self.balas = balas
    
    def porcentaje_vida(self):
        return self.vida
    
    def restar_vida(self, puntos):
        self.vida -= puntos
    
    def restar_balas(self, nro_balas):
        self.balas -= nro_balas
    
    
    def atacar_arma(self, victima):
        if self.balas > 0:
            danio = random.randint(1, 30)

            if self.balas > 20:
                balas = random.randint(5, 20)
            else:
                balas = random.randint(1, self.balas)

            print(f"{self.nombre} a atacado con pistola a {victima.nombre}")
            print(f"le ha hecho {danio} de daño y ha gastado {balas} balas")
            victima.restar_vida(danio)
            self.restar_balas(balas)
        else:
            print("Ya no te quedan balas")



class Terroristas(Personajes):
    def __init__(self, vida, nombre, vendas, balas):
        super().__init__(vida, nombre, vendas, balas)
        self.arrestado = False


    def atacar_cuchillo(self, victima):
        danio = random.randint(1, 8)
        print(f"{self.nombre} a atacado con cuchillo a {victima.nombre}")
        print(f"le ha hecho {danio} de daño")
        victima.restar_vida(danio)


    def curarse(self):
        if self.vida >= 70:
            print("No puede curarse porque todavía tiene más de 70 de vida")
        elif self.vendas == 0:
            print("Ya usó todas las vendas que tenía disponible")
        else:
            self.vida += 10



class Policias(Personajes):
    def __init__(self, vida, nombre, vendas, balas):
        super().__init__(vida, nombre, vendas, balas)


    def curarse(self):
        if self.vida >= 70:
            print("No puede curarse porque todavía tiene más de 70 de vida")
        elif self.vendas == 0:
            print("Ya usó todas las vendas que tenía disponible")
        else:
            self.vida += 20

    def arrestar(self, victima):
            victima.arrestado = True




def main():
    policia = Policias(100, "policia-Nico", 10, 120)
    terrorista = Terroristas(100, "terrorista-Ivan", 5, 120)
    
    while policia.porcentaje_vida() > 0 and terrorista.porcentaje_vida() > 0 and not terrorista.arrestado:
        os.system("cls")

        print("                             Policias vs terroristas\n")

        print("\nLa vida restante de ambos personajes es:")
        print(f"Policía: {policia.porcentaje_vida()}")
        print(f"Terrorista: {terrorista.porcentaje_vida()}")
        input("\nPresiona enter para continuar..\n")
        
        
        policia.atacar_arma(terrorista)
        input("\nPresiona enter para continuar..\n")
        
        if terrorista.porcentaje_vida() > 0:
            if terrorista.balas > 0:
                terrorista.atacar_arma(policia)
                input("\nPresiona enter para continuar..\n")
            else:
                terrorista.atacar_cuchillo(policia)
                input("\nPresiona enter para continuar..\n")

        if terrorista.porcentaje_vida() < 10 and terrorista.porcentaje_vida() > 0 and policia.porcentaje_vida() > 0:
            print("Lo harrestaste!!")
            policia.arrestar(terrorista)
            input("\nPresiona enter para continuar..\n")


    if policia.porcentaje_vida() <= 0:
        print("\nHan ganado los terroristas!!!")
        print(f"{terrorista.nombre} ha matado al {policia.nombre}")
    elif terrorista.arrestado:
        print("\nHan ganado los policias!!!")
        print(f"{policia.nombre} ha arrestado a {terrorista.nombre}")
    else:
        print("\nHan ganado los policias!!!")
        print(f"{policia.nombre} ha matado a {terrorista.nombre}")

    print("\nFin del juego")

if __name__ == "__main__":
    main()