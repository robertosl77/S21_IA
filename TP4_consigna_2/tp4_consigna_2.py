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

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread("TP4_consigna_2/img/img5.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar detección de bordes utilizando el algoritmo Canny
bordes = cv2.Canny(imagen, 50, 150, apertureSize=3)

# Aplicar la Transformada de Hough para detectar líneas en la imagen de bordes
lineas = cv2.HoughLinesP(
    bordes,
    rho=1,
    theta=np.pi / 180,
    threshold=150,            # Aumentar el umbral para detectar menos líneas no deseadas
    minLineLength=70,         # Longitud mínima que debe tener una línea para ser considerada
    maxLineGap=5              # Máxima separación entre segmentos para ser considerados una misma línea
)

# Crear una copia de la imagen original en color para dibujar las líneas detectadas
imagen_con_lineas = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

# Dibujar las líneas detectadas en la imagen
if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen_con_lineas, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Dibujar en color rojo

# Mostrar la imagen original y la imagen con las líneas detectadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(imagen, cmap="gray")
ax1.set_title("Imagen Original")
ax1.axis("off")

ax2.imshow(imagen_con_lineas)
ax2.set_title("Líneas Detectadas")
ax2.axis("off")

plt.show()
