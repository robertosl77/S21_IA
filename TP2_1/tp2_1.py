# Grafo actualizado según la corrección
arbol = {
    'B': ['B2', 'B1'],  # Intercambio el orden de B2 por B1 para que vaya por una rama sin solucion.
    'B1': ['B4', 'B3'],
    'B2': ['B6'],
    'B3': ['A'],
    'B4': ['B5'],
    'B5': [],
    'B6': [],
    'A': []
}

# Inicializamos el contador global del paso
paso = 1

# Función DFS modificada
def dfs(arbol, inicio, meta, camino=None, explorado=None):
    global paso
    
    if camino is None:
        camino = []
    if explorado is None:
        explorado = []
    
    # Agrego inicio a camino y explorados 
    camino.append(inicio)
    explorado.append(inicio)

    # Verificar si llegamos al nodo meta
    if inicio == meta:
        print(f"Meta alcanzada en el paso {paso}: Nodo actual: {inicio}, Nodos explorados: {', '.join(explorado)}")
        return True

    # Imprimir el estado actual
    siguiente = arbol[inicio][0] if arbol[inicio] else 'None'
    print(f"Paso {paso}: Nodo actual: {inicio}, Nodos explorados: {', '.join(explorado)}, Siguiente nodo: {siguiente}")
    
    # Incrementar paso global después de cada paso
    paso += 1

    for nodo in arbol[inicio]:
        if nodo not in explorado:
            result = dfs(arbol, nodo, meta, camino, explorado)
            if result:  # Si se ha alcanzado el objetivo, detener la búsqueda
                return True

    # Si no hay más nodos por explorar, retroceder
    camino.pop()
    return False

# Función para ejecutar DFS y generar la tabla de pasos
def print_dfs_steps():
    inicio = 'B'
    meta = 'A'
    camino = []
    explorados = []
    
    # Ejecutar DFS e imprimir la tabla en cada paso
    dfs(arbol, inicio, meta, camino, explorados)

# Ejecutar la función
print_dfs_steps()
