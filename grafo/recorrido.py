from collections import deque
from grafo.grafo_base import Grafo


class GrafoConRecorridos(Grafo):
    
    
    def dfs(self, inicio, objetivo, visitados=None):
        #Búsqueda en profundidad (DFS).
        
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        if inicio == objetivo:
            return [inicio]
        for vecino in self.grafo[inicio]:
            if vecino not in visitados:
                camino = self.dfs(vecino, objetivo, visitados)
                if camino:
                    return [inicio] + camino
        return None

    def bfs(self, inicio, objetivo):
        #Búsqueda en anchura (BFS).
        
        visitados = set()
        cola = deque([[inicio]])
        while cola:
            camino = cola.popleft()
            nodo = camino[-1]
            if nodo == objetivo:
                return camino
            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in self.grafo[nodo]:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)
        return None