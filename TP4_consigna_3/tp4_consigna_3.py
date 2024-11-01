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
import cv2                       # OpenCV: biblioteca para procesamiento de imágenes y visión por computadora. Proporciona herramientas avanzadas para manipulación y análisis de imágenes.
import numpy as np               # NumPy: biblioteca para manipulación eficiente de arreglos y matrices multidimensionales, muy utilizada en cálculos numéricos y álgebra lineal.
import matplotlib.pyplot as plt  # Matplotlib: biblioteca para visualización de datos en gráficos, especialmente útil para mostrar imágenes y resultados de procesamiento.

# Cargar la imagen en escala de grises
imagen = cv2.imread("TP4_consigna_3/img/img5.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar un suavizado para reducir el ruido antes de la detección de bordes
imagen_suavizada = cv2.medianBlur(imagen, 5)

# Aplicar la Transformada de Hough para detectar circunferencias
# dp controla la resolución de la imagen de acumulación (valores más altos mejoran la precisión)
# minDist es la distancia mínima entre los centros de las circunferencias detectadas para evitar superposiciones
# param1 define el umbral para el algoritmo Canny en la detección de bordes
# param2 establece el umbral de acumulación para la detección de circunferencias en la Transformada de Hough
# minRadius y maxRadius limitan el tamaño de los radios de las circunferencias detectadas
circulos = cv2.HoughCircles(
    imagen_suavizada,
    cv2.HOUGH_GRADIENT,
    dp=0.9,                # Incrementar el valor ligeramente para mayor precisión
    minDist=40,            # Aumentar para evitar superposiciones de círculos cercanos
    param1=180,            # Mayor valor para reducir el ruido en detección de bordes
    param2=50,             # Aumentar para reducir detecciones falsas
    minRadius=25,          # Ajustar a un valor mínimo según el tamaño de los elementos relevantes
    maxRadius=60           # Ajustar el máximo para evitar capturar elementos demasiado grandes
)

# Crear una copia de la imagen original en color para dibujar las circunferencias detectadas
imagen_con_circulos = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

# Dibujar las circunferencias detectadas
# Si se detectan circunferencias, redondear las coordenadas y radio para facilitar el dibujo
if circulos is not None:
    circulos = np.round(circulos[0, :]).astype("int")  # Convertir a enteros
    for (x, y, radio) in circulos:
        # Dibujar el contorno de la circunferencia
        cv2.circle(imagen_con_circulos, (x, y), radio, (0, 255, 0), 2)  # Color verde
        # Dibujar el centro de la circunferencia
        cv2.circle(imagen_con_circulos, (x, y), 3, (0, 0, 255), 3)     # Color rojo

# Mostrar la imagen original y la imagen con las circunferencias detectadas
# Crear una visualización en dos subgráficos: la imagen original y la imagen con circunferencias detectadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(imagen, cmap="gray")
ax1.set_title("Imagen Original")
ax1.axis("off")

ax2.imshow(imagen_con_circulos)
ax2.set_title("Circunferencias Detectadas")
ax2.axis("off")

# Mostrar la figura resultante con las dos imágenes
plt.show()
