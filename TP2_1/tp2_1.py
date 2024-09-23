'''
Inteligencia Artificial - TP2 - Punto 1

Comisión: CATEDRA - A - INF404 - EDH
Alumno: Roberto Sánchez Leiva
DNI: 25784362
Legajo: VINF012641
Titular Experto: PABLO ALEJANDRO VIRGOLINI
Titular Disciplinar: MARIA PAULA GONZALEZ
Fecha de Entrega: 30/09/2024
'''

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
    siguiente = arbol[inicio][0] if arbol[inicio] else 'Fin de la rama'
    print(f"Paso {paso}: Nodo actual: {inicio}, Nodos explorados: {', '.join(explorado)}, Siguiente nodo: {siguiente}")
    
    # Incrementar paso global después de cada paso
    paso += 1

    for nodo in arbol[inicio]:                                      # Recorro el sub-arbol
        if nodo not in explorado:                                   # valido que el nodo iterado no se haya recorrido anteriormente
            result = dfs(arbol, nodo, meta, camino, explorado)      # aplico recursividad sobre el metodo
            if result:                                              # Si se ha alcanzado el objetivo, detener la búsqueda
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
