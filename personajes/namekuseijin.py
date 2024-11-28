from personajes.personaje_base import Personaje

class Namekuseijin(Personaje):

    def __init__(self, nombre, nivel_poder=900, habilidades=None):
        super().__init__(nombre, "Namekuseijin", nivel_poder, habilidades)
        self.regeneraciones = 0

    def regenerar(self):
        
        self.nivel_poder_base += 500
        self.nivel_poder += 500
        self.regeneraciones += 1
        print(f"{self.nombre} ha usado regeneración. Poder base: {self.nivel_poder_base}, Poder actual: {self.nivel_poder}")

    def combatir(self, otro_personaje):

        print(f"¡{self.nombre} está combatiendo contra {otro_personaje.nombre}!")
        if self.nivel_poder > otro_personaje.nivel_poder:
            print(f"{self.nombre} gana el combate.")
            return self
        elif self.nivel_poder < otro_personaje.nivel_poder:
            print(f"{otro_personaje.nombre} gana el combate.")
            return otro_personaje
        else:
            print("El combate terminó en empate.")
            return None