'''
Inteligencia Artificial - TP4 - Consigna #2

Comisión: CATEDRA - A - INF404 - EDH
Alumno: Roberto Sánchez Leiva
DNI: 25784362
Legajo: VINF012641
Titular Experto: PABLO ALEJANDRO VIRGOLINI
Titular Disciplinar: MARIA PAULA GONZALEZ
Fecha de Entrega: 18/11/2024

Instalación necesaria: 
    - pip install opencv-python
    - pip install matplotlib
'''
import cv2  # OpenCV: biblioteca para procesamiento de imágenes y visión por computadora
import numpy as np  # NumPy: biblioteca para manipulación de matrices y cálculos numéricos
import matplotlib.pyplot as plt  # Matplotlib: biblioteca para generar gráficos y visualizar datos

# Cargar la imagen en escala de grises
imagen = cv2.imread("TP4_consigna_2/img/img5.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar detección de bordes utilizando el algoritmo Canny
# La función Canny detecta bordes en una imagen aplicando un filtro de gradiente
# Se configuran umbrales de detección de bordes (50 y 150) y el tamaño de la apertura (apertureSize=3)
bordes = cv2.Canny(imagen, 50, 150, apertureSize=3)

# Aplicar la Transformada de Hough para detectar líneas en la imagen de bordes
# El parámetro rho define la resolución en píxeles de la distancia radial
# theta establece la resolución angular en radianes
# threshold es el umbral mínimo de acumulación para detectar una línea
# minLineLength es la longitud mínima de línea para ser detectada
# maxLineGap permite la distancia máxima entre segmentos de línea para ser considerada una misma línea
lineas = cv2.HoughLinesP(
    bordes,                   # La imagen de bordes detectados, generada por el algoritmo Canny. Este es el input para la Transformada de Hough, que necesita los bordes detectados para buscar líneas rectas.
    rho=1,                    # La resolución en píxeles de la distancia radial en la Transformada de Hough. Al establecer rho en 1, cada unidad en el espacio de Hough equivale a un píxel en la imagen original.
    theta=np.pi / 180,        # La resolución angular en radianes para la Transformada de Hough. Al establecerla en np.pi / 180, se define una resolución de 1 grado (en radianes) para los ángulos de las líneas.
    threshold=150,            # Aumentar el umbral para detectar menos líneas no deseadas
    minLineLength=70,         # Longitud mínima que debe tener una línea para ser considerada
    maxLineGap=5              # Máxima separación entre segmentos para ser considerados una misma línea
)

# Crear una copia de la imagen original en color para dibujar las líneas detectadas
imagen_con_lineas = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

# Dibujar las líneas detectadas en la imagen
# Si se detectan líneas, se dibujan en color rojo (255, 0, 0) con un grosor de 2 píxeles
if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen_con_lineas, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Dibujar en color rojo

# Mostrar la imagen original y la imagen con las líneas detectadas
# Crear una visualización en dos subgráficos: la imagen original y la imagen con líneas detectadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(imagen, cmap="gray")
ax1.set_title("Imagen Original")
ax1.axis("off")

ax2.imshow(imagen_con_lineas)
ax2.set_title("Líneas Detectadas")
ax2.axis("off")

# Mostrar la figura resultante con las dos imágenes
plt.show()
