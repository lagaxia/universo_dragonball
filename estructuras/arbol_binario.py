class Nodo:
    
    def __init__(self, personaje):
        self.personaje = personaje  
        self.izquierdo = None
        self.derecho = None


#Árbol Binario de Búsqueda para organizar personajes por nivel de poder.
class ArbolBinario:
    
    def __init__(self):
        self.raiz = None
    
    def insertar(self, personaje):
        
        nuevo_nodo = Nodo(personaje)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)
    
    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.personaje.nivel_poder < nodo_actual.personaje.nivel_poder:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecho, nuevo_nodo)
    
    def buscar(self, nivel_poder):
        
        return self._buscar_recursivo(self.raiz, nivel_poder)
    
    def _buscar_recursivo(self, nodo_actual, nivel_poder):
        if nodo_actual is None:
            return None
        if nodo_actual.personaje.nivel_poder == nivel_poder:
            return nodo_actual.personaje
        elif nivel_poder < nodo_actual.personaje.nivel_poder:
            return self._buscar_recursivo(nodo_actual.izquierdo, nivel_poder)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, nivel_poder)
    
    def recorrido_inorden(self):
        #Devuelve una lista de personajes en orden ascendente de nivel de poder.
        
        resultado = []
        self._recorrido_inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _recorrido_inorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual is not None:
            self._recorrido_inorden_recursivo(nodo_actual.izquierdo, resultado)
            resultado.append(nodo_actual.personaje)
            self._recorrido_inorden_recursivo(nodo_actual.derecho, resultado)