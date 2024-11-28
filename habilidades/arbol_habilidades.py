class NodoHabilidad:
    
    def __init__(self, nombre, nivel=1):
        self.nombre = nombre
        self.nivel = nivel
        self.hijos = []

    def agregar_hijo(self, habilidad):
        
        self.hijos.append(habilidad)

    def subir_nivel(self): #Sube de nivel la habilidad actual hasta un máximo de 3.
        
        if self.nivel < 3:
            self.nivel += 1
            print(f"La habilidad {self.nombre} ha subido al nivel {self.nivel}.")
        else:
            print(f"La habilidad {self.nombre} ya está en el nivel máximo.")

class ArbolHabilidades:
    
    def __init__(self, raiz):
        self.raiz = NodoHabilidad(raiz)

    def agregar_habilidad(self, habilidad_padre, nueva_habilidad):
        
        nodo_padre = self._buscar(self.raiz, habilidad_padre)
        if nodo_padre:
            nodo_padre.agregar_hijo(NodoHabilidad(nueva_habilidad))
            print(f"Habilidad '{nueva_habilidad}' agregada como derivada de '{habilidad_padre}'.")
        else:
            print(f"No se encontro la habilidad '{habilidad_padre}'.")

    def _buscar(self, nodo_actual, habilidad):
        
        if nodo_actual.nombre == habilidad:
            return nodo_actual
        for hijo in nodo_actual.hijos:
            encontrado = self._buscar(hijo, habilidad)
            if encontrado:
                return encontrado
        return None

    def mostrar_arbol(self, nodo=None, nivel=0):
        
        if nodo is None:
            nodo = self.raiz
        print(" " * (nivel * 2) + f"{nodo.nombre} (Nivel {nodo.nivel})")
        for hijo in nodo.hijos:
            self.mostrar_arbol(hijo, nivel + 1)
