import heapq
from grafo.recorrido import GrafoConRecorridos

class GrafoConDijkstra(GrafoConRecorridos):
    #extiende la clase Grafo para encontrar caminos mínimos.

    def dijkstra(self, inicio):
        
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[inicio] = 0
        cola = [(0, inicio)]

        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)
            for vecino, peso in self.grafo[nodo_actual].items():
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola, (distancia, vecino))
        return distancias