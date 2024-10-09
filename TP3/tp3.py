'''
Inteligencia Artificial - TP3

Comisión: CATEDRA - A - INF404 - EDH
Alumno: Roberto Sánchez Leiva
DNI: 25784362
Legajo: VINF012641
Titular Experto: PABLO ALEJANDRO VIRGOLINI
Titular Disciplinar: MARIA PAULA GONZALEZ
Fecha de Entrega: 21/10/2024

Importante, ejecutar esta clase
'''
from constantes import patron1, patron2, patron3, patron4, patron5, imagen_ruido  # Importamos las matrices desde constantes.py
from hopfield import convertir_a_hopfield_matriz, entrenar_hopfield, mostrar_matriz, limpiar_hopfield

class TP3:
    def __init__(self) -> None:
        self.ejecuta_proyecto()

    def ejecuta_proyecto(self): 
        print("Patron1: imagen ligeramente alineada arriba a la izquierda\n" + '\n'.join([' '.join(map(str, fila)) for fila in patron1]) + "\n")
        print("Patron2: imagen ligeramente alineada arriba a la derecha\n" + '\n'.join([' '.join(map(str, fila)) for fila in patron2]) + "\n")
        print("Patron3: imagen alineada arriba a la derecha\n" + '\n'.join([' '.join(map(str, fila)) for fila in patron3]) + "\n")
        print("Patron4: imagen ligeramente alineada abajo a la izquierda\n" + '\n'.join([' '.join(map(str, fila)) for fila in patron4]) + "\n")
        print("Patron5: imagen ligeramente alineada abajo a la derecha\n" + '\n'.join([' '.join(map(str, fila)) for fila in patron5]) + "\n")

        # Convertimos las matrices de entrenamiento a formato Hopfield (-1 y 1)
        patron1_hopfield = convertir_a_hopfield_matriz(patron1)
        patron2_hopfield = convertir_a_hopfield_matriz(patron2)
        patron3_hopfield = convertir_a_hopfield_matriz(patron3)
        patron4_hopfield = convertir_a_hopfield_matriz(patron4)
        patron5_hopfield = convertir_a_hopfield_matriz(patron5)

        # Entrenamos el modelo de Hopfield con las matrices de entrenamiento
        patrones_entrenamiento = [patron1_hopfield, patron2_hopfield, patron3_hopfield, patron4_hopfield, patron5_hopfield]
        pesos_entrenados = entrenar_hopfield(patrones_entrenamiento)

        # Mostramos la imagen con ruido antes de limpiarla
        print("Imagen con ruido antes de limpieza:")
        mostrar_matriz(imagen_ruido)

        # Convertimos la imagen con ruido al formato Hopfield (-1 y 1)
        imagen_ruido_hopfield = convertir_a_hopfield_matriz(imagen_ruido)

        # Aplicamos el modelo de Hopfield para intentar limpiar la imagen ruidosa
        imagen_limpia = limpiar_hopfield(pesos_entrenados, imagen_ruido_hopfield)

        # Mostramos la imagen después de ser limpiada
        print("Imagen después de limpieza con Hopfield:")
        mostrar_matriz(imagen_limpia)




tp3= TP3()