from personajes.personaje_base import Personaje

class Saiyajin(Personaje):

    def __init__(self, nombre, nivel_poder=1000, habilidades=None):
        super().__init__(nombre, "Saiyajin", nivel_poder, habilidades)
        self.transformaciones = []  #Lista de transformaciones desbloqueadas

    def agregar_transformacion(self, transformacion):
        
        transformaciones_validas = ["Kaioken", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"]
        
        if transformacion not in transformaciones_validas:
            print(f"{transformacion} no es una transformacion valida.")
            return
        
        if transformacion not in self.transformaciones:
            self.transformaciones.append(transformacion)
            multiplicadores = {
                "Kaioken": 4,
                "Super Saiyajin": 50,
                "Super Saiyajin 2": 100,
                "Super Saiyajin 3": 300,
            }
            self.multiplicadores[transformacion] = multiplicadores[transformacion]
            print(f"{self.nombre} ha desbloqueado la transformacion: {transformacion}")
        else:
            print(f"{self.nombre} ya tiene la transformación: {transformacion}")

    def transformarse(self, transformacion): #se transforma aumentando el poder base (de forma temporal)

        if transformacion not in self.transformaciones:
            print(f"{self.nombre} no tiene desbloqueada la transformacion: {transformacion}")
            return

        self.transformacion_activa = transformacion
        self.evolucionar_poder_recursivo(1, self.multiplicadores[transformacion])

    def destransformarse(self):
        
        if self.transformacion_activa:
            print(f"{self.nombre} ha regresado a su estado base.")
            self.transformacion_activa = None
            self.nivel_poder = self.nivel_poder_base
        else:
            print(f"{self.nombre} ya está en su estado base.")

    def combatir(self, otro_personaje):

        print(f"¡{self.nombre} está combatiendo contra {otro_personaje.nombre}!")
        if self.nivel_poder > otro_personaje.nivel_poder:
            print(f"{self.nombre} gana el combate.")
            return self
        elif self.nivel_poder < otro_personaje.nivel_poder:
            print(f"{otro_personaje.nombre} gana el combate.")
            return otro_personaje
        else:
            print("El combate terminóo en empate.")
            return None