class Entrenamiento:
    
    def __init__(self):
        self.grafo = {}

    def agregar_habilidad(self, habilidad):

        if habilidad not in self.grafo:
            self.grafo[habilidad] = []

    def agregar_dependencia(self, prerequisito, habilidad): #Agrega una arista (prerequisito -> habilidad).

        if prerequisito in self.grafo:
            self.grafo[prerequisito].append(habilidad)
        else:
            self.grafo[prerequisito] = [habilidad]

    def orden_topologico(self): 
        
        visitados = set()
        stack = []

        def dfs(nodo):
            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in self.grafo.get(nodo, []):
                    dfs(vecino)
                stack.append(nodo)

        for nodo in self.grafo:
            dfs(nodo)
        return stack[::-1]