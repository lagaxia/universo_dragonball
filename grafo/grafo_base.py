
#Clase que representa el universo de Dragon Ball como un grafo.
class Grafo:
    
    def __init__(self):
        self.grafo = {}

    def agregar_planeta(self, planeta):
        
        if planeta not in self.grafo:
            self.grafo[planeta] = {}
            print(f"Planeta {planeta} agregado al universo.")

    def agregar_ruta(self, origen, destino, distancia):
        
        if origen in self.grafo and destino in self.grafo:
            self.grafo[origen][destino] = distancia
            self.grafo[destino][origen] = distancia  # Grafo no dirigido
            print(f"Ruta agregada: {origen} <-> {destino} (Distancia: {distancia})")
        else:
            print("Ambos planetas deben existir en el grafo.")

    def mostrar_grafo(self):
        
        for planeta, rutas in self.grafo.items():
            print(f"{planeta}: {rutas}")