from personajes.saiyajin import Saiyajin
from personajes.namekuseijin import Namekuseijin
from habilidades.arbol_habilidades import ArbolHabilidades
from estructuras.arbol_binario import ArbolBinario
from grafo.grafo_base import Grafo
from grafo.recorrido import GrafoConRecorridos
from grafo.dijkstra import GrafoConDijkstra
from estructuras.cola_de_prioridad import ColaDePrioridad
from habilidades.entrenamiento import Entrenamiento

#Prueba de todo lo visto: #

def main():
    # --- Parte 1: Creación de Personajes --- #
    print("\n=== Parte 1: Creación de Personajes ===")
    goku = Saiyajin("Goku", nivel_poder=15000)
    vegeta = Saiyajin("Vegeta", nivel_poder=14000)
    piccolo = Namekuseijin("Piccolo", nivel_poder=12000)

    # Agregar habilidades #
    goku.agregar_habilidad("Kamehameha")
    vegeta.agregar_habilidad("Galick Gun")
    piccolo.agregar_habilidad("Makankosappo")

    # Desbloquear y activar transformaciones #
    goku.agregar_transformacion("Super Saiyajin")
    goku.transformarse("Super Saiyajin")
    vegeta.agregar_transformacion("Super Saiyajin")
    vegeta.transformarse("Super Saiyajin")

    # Mostrar estadísticas #
    goku.mostrar_estadisticas()
    vegeta.mostrar_estadisticas()
    piccolo.mostrar_estadisticas()

    # --- Parte 2: Árbol de Habilidades --- #
    print("\n=== Parte 2: Árbol de Habilidades ===")
    arbol_habilidades = ArbolHabilidades("Kamehameha")
    arbol_habilidades.agregar_habilidad("Kamehameha", "Kamehameha x10")
    arbol_habilidades.agregar_habilidad("Kamehameha x10", "Kamehameha Final")
    arbol_habilidades.mostrar_arbol()

    # Subir nivel de habilidades #
    nodo_kamehameha = arbol_habilidades._buscar(arbol_habilidades.raiz, "Kamehameha")
    nodo_kamehameha.subir_nivel()

    # --- Parte 3: Torneo con Cola de Prioridad --- #
    print("\n=== Parte 3: Torneo ===")
    cola_torneo = ColaDePrioridad()
    cola_torneo.agregar_personaje(goku)
    cola_torneo.agregar_personaje(vegeta)
    cola_torneo.agregar_personaje(piccolo)

    # Mostrar orden del torneo #
    print("Orden del torneo (Nivel de Poder):", cola_torneo.mostrar_orden())

    # Realizar combates #
    while True:
        siguiente = cola_torneo.siguiente_combate()
        if not siguiente:
            break
        print(f"Combate asignado para: {siguiente[1]} (Nivel de Poder: {-siguiente[0]})")

    # --- Parte 4: Árbol Binario de Personajes --- #
    print("\n=== Parte 4: Árbol Binario de Personajes ===")
    arbol_personajes = ArbolBinario()
    arbol_personajes.insertar(goku)
    arbol_personajes.insertar(vegeta)
    arbol_personajes.insertar(piccolo)

    # Buscar un personaje  #
    nivel_buscar = 15000  
    personaje_fuerte = arbol_personajes.buscar(nivel_buscar)

    if personaje_fuerte:
        print(f"Personaje encontrado con nivel {nivel_buscar}: {personaje_fuerte.nombre}")
    else:
        print(f"No se encontró ningun personaje con nivel de poder {nivel_buscar}.")

    # Mostrar personajes en orden ascendente de nivel de poder #
    print("Personajes ordenados por nivel de poder:")
    for personaje in arbol_personajes.recorrido_inorden():
        print(f"{personaje.nombre} - Nivel de Poder: {personaje.nivel_poder}")


    # --- Parte 5: Grafos del Universo y Rutas ---- #
    print("\n=== Parte 5: Universo de Dragon Ball ===")
    universo = GrafoConDijkstra()
    universo.agregar_planeta("Tierra")
    universo.agregar_planeta("Namek")
    universo.agregar_planeta("Vegeta")
    universo.agregar_planeta("Kaiosama")

    # Agregar rutas espaciales #
    universo.agregar_ruta("Tierra", "Namek", 5000)
    universo.agregar_ruta("Tierra", "Vegeta", 8000)
    universo.agregar_ruta("Namek", "Kaiosama", 10000)
    universo.agregar_ruta("Vegeta", "Kaiosama", 6000)

    # Mostrar grafo del universo #
    universo.mostrar_grafo()

    # DFS y BFS
    print("DFS (Tierra -> Kaiosama):", universo.dfs("Tierra", "Kaiosama"))
    print("BFS (Tierra -> Kaiosama):", universo.bfs("Tierra", "Kaiosama"))

    # Dijkstra: Camino Mínimo #
    distancias = universo.dijkstra("Tierra")
    print("Distancias desde Tierra:", distancias)

    # ---- parte 6: Ordenamiento Topologico de Entrenamiento --- #
    print("\n=== Parte 6: Entrenamiento ===")
    entrenamiento = Entrenamiento()
    entrenamiento.agregar_habilidad("Kamehameha")
    entrenamiento.agregar_habilidad("Kamehameha x10")
    entrenamiento.agregar_habilidad("Kamehameha Final")
    entrenamiento.agregar_dependencia("Kamehameha", "Kamehameha x10")
    entrenamiento.agregar_dependencia("Kamehameha x10", "Kamehameha Final")

    # Orden topologico #
    print("Orden de entrenamiento:", entrenamiento.orden_topologico())


if __name__ == "__main__":
    main()

