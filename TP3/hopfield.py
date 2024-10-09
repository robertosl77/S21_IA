import numpy as np

# Función para entrenar el modelo de Hopfield
def entrenar_hopfield(patrones):
    """
    Entrena el modelo de Hopfield basado en los patrones de entrada.
    Devuelve la matriz de pesos entrenada.
    """
    num_neuronas = patrones[0].size  # Número de neuronas es el tamaño total de cada patrón (10x10 = 100 neuronas)
    pesos = np.zeros((num_neuronas, num_neuronas))  # Inicializamos la matriz de pesos a ceros

    for patron in patrones:
        patron_vector = patron.flatten()  # Aplanamos el patrón (matriz) a un vector de una dimensión
        pesos += np.outer(patron_vector, patron_vector)  # Aplicamos la regla de Hebb para ajustar los pesos

    np.fill_diagonal(pesos, 0)  # Nos aseguramos de que no haya auto-conexiones
    return pesos

# Función para limpiar una imagen con ruido utilizando el modelo Hopfield
def limpiar_hopfield(pesos, imagen_ruido, iteraciones=10):
    """
    Intenta limpiar una imagen ruidosa utilizando los pesos entrenados.
    Itera varias veces para actualizar el estado de la imagen.
    """
    estado = imagen_ruido.flatten()  # Aplanamos la imagen ruidosa a un vector

    for _ in range(iteraciones):
        for i in range(len(estado)):
            entrada_neta = np.dot(pesos[i], estado)  # Calculamos la entrada neta multiplicando pesos por estado actual
            estado[i] = 1 if entrada_neta >= 0 else -1  # Actualizamos el estado usando función de activación (signo)

    return estado.reshape((10, 10))  # Convertimos de nuevo el vector en matriz 10x10

# Función para convertir una matriz de 0s y 1s a -1 y 1 para Hopfield
def convertir_a_hopfield_matriz(matriz):
    """
    Convierte una matriz de 0s y 1s a la representación -1 y 1 para el modelo Hopfield.
    """
    return np.where(matriz == 0, -1, 1)

# Función para mostrar una imagen/matriz en consola
def mostrar_matriz(matriz):
    """
    Imprime una matriz de forma legible en la consola.
    """
    for fila in matriz:
        print(' '.join(['{:2}'.format(int(x)) for x in fila]))
    print("\n")
