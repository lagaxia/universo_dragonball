from abc import ABC, abstractmethod

class Personaje(ABC):

    def __init__(self, nombre, raza, nivel_poder=1000, habilidades=None):
        self.nombre = nombre
        self.raza = raza
        self.nivel_poder_base = nivel_poder  #Nivel de poder sin transformaciones
        self.nivel_poder = nivel_poder  # Nivel actual (transformado o base)
        self.habilidades = habilidades if habilidades else []
        self.multiplicadores = {}  #De transformaciones 
        self.transformacion_activa = None  

    def agregar_habilidad(self, habilidad):
        
        if habilidad not in self.habilidades:
            self.habilidades.append(habilidad)
            print(f"{self.nombre} ha aprendido la habilidad: {habilidad}")
        else:
            print(f"{self.nombre} ya conoce la habilidad: {habilidad}")
            
    def subir_nivel(self, incremento):

        self.nivel_poder_base += incremento 
        print(f"{self.nombre} subió de nivel. Nivel base: {self.nivel_poder_base}")
        if self.transformacion_activa:
            multiplicador = self.multiplicadores[self.transformacion_activa]
            self.nivel_poder = self.nivel_poder_base * multiplicador
        else:
            self.nivel_poder = self.nivel_poder_base

    def evolucionar_poder_recursivo(self, combates, multiplicador=1.1): #incremento recursivo luego de combates

        if combates == 0:
            return self.nivel_poder_base
        incremento = int(self.nivel_poder_base * (multiplicador - 1))
        self.subir_nivel(incremento)
        return self.evolucionar_poder_recursivo(combates - 1, multiplicador)

    @abstractmethod
    def combatir(self, otro_personaje):
        pass #se implementa en las subclases (metodo abstracto)
    
    
    def mostrar_estadisticas(self):
        
        estado = self.transformacion_activa if self.transformacion_activa else "Estado Base"
        print(f"{self.nombre} ({self.raza}): Poder Base: {self.nivel_poder_base}, Poder Actual: {self.nivel_poder}")
        print(f"Habilidades: {', '.join(self.habilidades) if self.habilidades else 'Ninguna'}")
        print(f"Estado Actual: {estado}")