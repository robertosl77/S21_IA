import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread("TP4_consigna_2/img/img4.jpg", cv2.IMREAD_GRAYSCALE)

bordes = cv2.Canny(imagen, 50, 150, apertureSize=3)

lineas = cv2.HoughLinesP(
    bordes,
    rho=1,
    theta=np.pi / 180,
    threshold=100,
    minLineLength=40,
    maxLineGap=10
)

imagen_con_lineas = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen_con_lineas, (x1, y1), (x2, y2), (255, 0, 0), 2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(imagen, cmap="gray")
ax1.set_title("Imagen Original")
ax1.axis("off")

ax2.imshow(imagen_con_lineas)
ax2.set_title("Líneas Detectadas")
ax2.axis("off")

plt.show()
