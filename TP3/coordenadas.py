import numpy as np

class Coordenadas:
    def __init__(self):
        pass

    # Función para calcular el centro del círculo
    def calcular_centro(self, matriz):
        """
        Calcula el centro del círculo (contorno de 1s) en la matriz.
        Retorna una tupla (centro_x, centro_y) o None si no se encuentra el círculo.
        """
        coordenadas_x = []
        coordenadas_y = []
        
        # Recorremos la matriz para encontrar las posiciones del contorno (píxeles 1)
        for i in range(matriz.shape[0]):
            for j in range(matriz.shape[1]):
                if matriz[i, j] == 1:  # Identificamos el contorno del círculo
                    coordenadas_x.append(i)
                    coordenadas_y.append(j)
        
        # Calculamos el promedio de las coordenadas (X, Y)
        if len(coordenadas_x) > 0 and len(coordenadas_y) > 0:
            centro_x = sum(coordenadas_x) / len(coordenadas_x)
            centro_y = sum(coordenadas_y) / len(coordenadas_y)
            return (centro_x, centro_y)
        else:
            return None  # Si no se encuentra un contorno, devolvemos None

    # Función para verificar si el aro está alineado
    def verificar_alineacion(self, centro, umbral_x=5, umbral_y=5):
        """
        Verifica si el aro está alineado comparando las coordenadas del centro con los umbrales.
        Retorna un mensaje indicando si el aro está alineado o no.
        """
        if centro:
            centro_x, centro_y = centro
            if abs(centro_x - umbral_x) <= 1 and abs(centro_y - umbral_y) <= 1:
                return "El aro está alineado"
            else:
                return f"El aro NO está alineado. Centro detectado en: ({centro_x}, {centro_y})"
        else:
            return "No se pudo identificar el aro."

