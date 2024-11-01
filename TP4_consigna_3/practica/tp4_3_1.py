import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread("TP4_consigna_3/img/img1.jpg", cv2.IMREAD_GRAYSCALE)

imagen_suavizada = cv2.medianBlur(imagen, 5)

circulos = cv2.HoughCircles(
    imagen_suavizada,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=50,
    param1=50,
    param2=40,
    minRadius=80,
    maxRadius=100
)

imagen_con_circulos = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

if circulos is not None:
    circulos = np.round(circulos[0, :]).astype("int")
    for (x, y, radio) in circulos:
        cv2.circle(imagen_con_circulos, (x, y), radio, (0, 255, 0), 2)
        cv2.circle(imagen_con_circulos, (x, y), 3, (0, 0, 255), 3)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(imagen, cmap="gray")
ax1.set_title("Imagen Original")
ax1.axis("off")

ax2.imshow(imagen_con_circulos)
ax2.set_title("Circunferencias Detectadas")
ax2.axis("off")

plt.show()
