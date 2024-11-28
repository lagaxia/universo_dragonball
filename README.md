# Universo Dragon Ball - Simulación con Python

## Descripción del Proyecto

Este proyecto implementa un sistema que simula el universo de Dragon Ball. Permite la creacion y gestión de personajes, habilidades, combates, torneos y viajes entre planetas utilizando estructuras de datos como arboles binarios, grafos y colas de prioridad.

El sistema está diseñado para ser modular y extensible, empleando principios de la programación orientada a objetos (POO). También se incluyen algoritmos como búsqueda DFS/BFS y Dijkstra para resolver problemas espaciales y de entrenamiento.

---

## Funcionalidades

- **Gestión de Personajes**:
  - Creación de personajes con atributos como nivel de poder, habilidades y raza (Saiyajin, Namekuseijin, etc.).
  - Sistema de transformaciones con multiplicadores de nivel de poder (Kaioken, Super Saiyajin, etc.).
  - Combates entre personajes con determinación del ganador.

- **Sistema de Habilidades**:
  - Árbol jerarquico de habilidades que modela dependencias entre técnicas (ejemplo: Kamehameha -> Kamehameha x10 -> Kamehameha Final).
  - Planificación de entrenamientos usando ordenamiento topologico en un grafo dirigido.

- **Estructuras de Datos*:
  - **Srbol Binario:** Organización de personajes por nivel de poder.
  - **Cola de Prioridad:** Gestión de torneos en función del nivel de poder de los participantes.

- **Universo de Dragon Ball**:
  - Representación del universo como un grafo, con nodos para planetas y aristas para rutas espaciales.
  - Búsqueda de caminos entre planetas usando DFS y BFS.
  - Cálculo de caminos mínimos (distancias mas cortas) entre planetas con Dijkstra.

---

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.13

## Instalación

1. **Clona el Repositorio**:
   ```bash
   git clone https://github.com/tuusuario/dragon-ball-game.git
