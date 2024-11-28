import heapq

class ColaDePrioridad:
    
    def __init__(self):
        self.cola = []

    def agregar_personaje(self, personaje):
        
        # Usamos valores negativos porque `heapq` es una min-heap por defecto
        heapq.heappush(self.cola, (-personaje.nivel_poder, personaje.nombre))

    def siguiente_combate(self):
        
        if self.cola:
            return heapq.heappop(self.cola)
        else:
            print("No hay más personajes en la cola.")
            return None

    def mostrar_orden(self):
        
        return [(-poder, nombre) for poder, nombre in self.cola]