import heapq

# Definimos el arbol represetnado en el documento. 
arbol = {
    'B': ['B1', 'B2'],
    'B1': ['B3', 'B4'],
    'B2': ['B6'],
    'B3': ['A'],
    'B4': ['B5'],
    'B5': [],
    'B6': [],
    'A' : []
}

# Definimos los valores de g(n) y h(n)
g = {
    'B': 0,
    'B1': 1,
    'B2': 1,
    'B3': 2,
    'B4': 2,
    'B5': 3,
    'B6': 3,
    'A': 4
}

h = {
    'B': 6,
    'B1': 4,
    'B2': 5,
    'B3': 1,
    'B4': 2,
    'B5': 3,
    'B6': 4,
    'A': 0
}

# Función A* (A-star)
def a_estrella(arbol, inicio, meta):
    # Cola de prioridad para los nodos abiertos (prioridad, nodo, camino actual)
    abiertos = []
    # Aplicamos libreria python para que ordene los nodos segun su valor heuristico
    heapq.heappush(abiertos, (h[inicio], inicio, [inicio])) # sirve para añadir un nodo con su valor heurístico a una lista de nodos abiertos, manteniéndolos ordenados.
    # Conjunto de nodos cerrados
    cerrados = set()
    # Iniciamos el paso
    paso = 1

    # Iteramos
    while abiertos:
        # Imprimir el estado actual de nodos abiertos y cerrados
        # print(f"Paso {paso}: Abiertos: {[f"{nodo}({h[nodo]})" for _, nodo, _ in abiertos][0]}, Cerrados: {list(cerrados)[0] if list(cerrados) != [] else ''}")
        # print(f"Paso {paso}: Abiertos: {[nodo for _, nodo, _ in abiertos]}, Cerrados: {list(cerrados)}")
        print(f"Paso {paso}: Abiertos: {[(nodo, f) for f, nodo, _ in abiertos]}, Cerrados: {list(cerrados)}")

        # Obtener el nodo con menor costo f(n) = g(n) + h(n)
        f_actual, nodo_actual, camino = heapq.heappop(abiertos) 
        
        paso += 1
        
        # Si llegamos al nodo meta, devolver el camino
        if nodo_actual == meta:
            print(f"Meta alcanzada: {camino}")
            return camino

        # Mover el nodo actual a cerrados
        cerrados.add(nodo_actual)

        # Explorar los vecinos del nodo actual
        for vecino in arbol[nodo_actual]:
            if vecino in cerrados:
                continue  # Saltar si el nodo ya está en cerrados

            g_nuevo = g[nodo_actual] + 1  # Actualizar g(n)
            f_nuevo = g_nuevo + h[vecino]  # Calcular f(n) = g(n) + h(n)
            
            # Agregar el vecino a la cola de prioridad si no está en cerrados
            heapq.heappush(abiertos, (f_nuevo, vecino, camino + [vecino]))

# Ejecutar el algoritmo A*
a_estrella(arbol, 'B', 'A')
