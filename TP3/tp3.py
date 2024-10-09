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
from coordenadas import Coordenadas
from matrices import Matrices
from hopfield import convertir_a_hopfield_matriz, entrenar_hopfield, mostrar_matriz, limpiar_hopfield, convertir_a_ceros_y_unos

class TP3:
    def __init__(self) -> None:
        self.ejecuta_proyecto()

    def ejecuta_proyecto(self): 
        coord = Coordenadas()
        const = Matrices()
        #
        const.imprime_patron(1,coord.calcular_centro(const.patron1))
        const.imprime_patron(2,coord.calcular_centro(const.patron2))
        const.imprime_patron(3,coord.calcular_centro(const.patron3))
        const.imprime_patron(4,coord.calcular_centro(const.patron4))
        const.imprime_patron(5,coord.calcular_centro(const.patron5))

        # Convertimos las matrices de entrenamiento a formato Hopfield (-1 y 1)
        patron1_hopfield = convertir_a_hopfield_matriz(const.patron1)
        patron2_hopfield = convertir_a_hopfield_matriz(const.patron2)
        patron3_hopfield = convertir_a_hopfield_matriz(const.patron3)
        patron4_hopfield = convertir_a_hopfield_matriz(const.patron4)
        patron5_hopfield = convertir_a_hopfield_matriz(const.patron5)

        # Entrenamos el modelo de Hopfield con las matrices de entrenamiento
        patrones_entrenamiento = [patron1_hopfield, patron2_hopfield, patron3_hopfield, patron4_hopfield, patron5_hopfield]
        pesos_entrenados = entrenar_hopfield(patrones_entrenamiento)

        # Mostramos la imagen con ruido antes de limpiarla
        print("Imagen con ruido antes de limpieza:")
        mostrar_matriz(const.imagen_ruido)

        # Convertimos la imagen con ruido al formato Hopfield (-1 y 1)
        imagen_ruido_hopfield = convertir_a_hopfield_matriz(const.imagen_ruido)

        # Aplicamos el modelo de Hopfield para intentar limpiar la imagen ruidosa
        imagen_limpia_hopfield = limpiar_hopfield(pesos_entrenados, imagen_ruido_hopfield)
        imagen_limpia = convertir_a_ceros_y_unos(imagen_limpia_hopfield)

        # Mostramos la imagen después de ser limpiada
        print("Imagen después de limpieza con Hopfield:")
        mostrar_matriz(imagen_limpia)

        # Calculamos indices de la imagen limpia
        print("Las coordenadas de la imagen limpia es: ",coord.calcular_centro(imagen_limpia))        

        # Usamos la clase Coordenadas para calcular el centro y verificar la alineación
        centro_aro = coord.calcular_centro(imagen_limpia)
        mensaje_alineacion = coord.verificar_alineacion(centro_aro)

        # Mostramos el resultado de alineación
        print(mensaje_alineacion)        




tp3= TP3()