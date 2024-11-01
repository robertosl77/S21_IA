'''
Inteligencia Artificial - TP4 - Consigna #3

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
imagen = cv2.imread("TP4_consigna_3/img/img2.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar un suavizado para reducir el ruido antes de la detección de bordes
imagen_suavizada = cv2.medianBlur(imagen, 5)

# Aplicar la Transformada de Hough para detectar circunferencias
circulos = cv2.HoughCircles(
    imagen_suavizada,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=50,
    param1=50,               # Mantener similar para el umbral de Canny
    param2=40,               # Aumentar para reducir la sensibilidad a círculos falsos
    minRadius=80,            # Ajustar según el tamaño del círculo grande
    maxRadius=100            # Ajustar para que no detecte círculos más pequeños
)

# Crear una copia de la imagen original en color para dibujar las circunferencias detectadas
imagen_con_circulos = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

# Dibujar las circunferencias detectadas
if circulos is not None:
    circulos = np.round(circulos[0, :]).astype("int")  # Convertir a enteros
    for (x, y, radio) in circulos:
        # Dibujar el contorno de la circunferencia
        cv2.circle(imagen_con_circulos, (x, y), radio, (0, 255, 0), 2)  # Color verde
        # Dibujar el centro de la circunferencia
        cv2.circle(imagen_con_circulos, (x, y), 3, (0, 0, 255), 3)     # Color rojo

# Mostrar la imagen original y la imagen con las circunferencias detectadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(imagen, cmap="gray")
ax1.set_title("Imagen Original")
ax1.axis("off")

ax2.imshow(imagen_con_circulos)
ax2.set_title("Circunferencias Detectadas")
ax2.axis("off")

plt.show()
