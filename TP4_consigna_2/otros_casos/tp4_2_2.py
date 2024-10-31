'''
Inteligencia Artificial - TP4 - Consigna #2

Comisión: CATEDRA - A - INF404 - EDH
Alumno: Roberto Sánchez Leiva
DNI: 25784362
Legajo: VINF012641
Titular Experto: PABLO ALEJANDRO VIRGOLINI
Titular Disciplinar: MARIA PAULA GONZALEZ
Fecha de Entrega: 18/11/2024

Instalacion necesaria: 
    -pip install opencv-python
    -pip install matplotlib

'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen
imagen = cv2.imread("TP4_consigna_2/img/img2.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar detección de bordes con Canny
bordes = cv2.Canny(imagen, 50, 150, apertureSize=3)

# Aplicar Transformada de Hough para líneas
lineas = cv2.HoughLinesP(
    bordes,
    rho=1,
    theta=np.pi / 180,
    threshold=100,           # Aumentar el umbral para reducir líneas
    minLineLength=40,         # Definir longitud mínima
    maxLineGap=10             # Definir separación máxima entre segmentos
)

# lineas = cv2.HoughLinesP(
#     bordes,
#     rho=1,
#     theta=np.pi / 180,
#     threshold=120,           # Aumentar aún más el umbral para reducir líneas irrelevantes
#     minLineLength=80,         # Aumentar la longitud mínima
#     maxLineGap=5              # Reducir la separación máxima entre segmentos
# )

# Crear una copia de la imagen original para dibujar las líneas
imagen_con_lineas = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

# Dibujar las líneas detectadas
if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen_con_lineas, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Mostrar imagen original y con líneas detectadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(imagen, cmap="gray")
ax1.set_title("Imagen Original")
ax1.axis("off")

ax2.imshow(imagen_con_lineas)
ax2.set_title("Líneas Detectadas")
ax2.axis("off")

plt.show()
