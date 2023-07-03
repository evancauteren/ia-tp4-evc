# Importamos las librerías necesarias
import cv2
import numpy as np

# Cargamos una imagen de entrada a color
image = cv2.imread('entrada_lineas.jpg', cv2.IMREAD_COLOR)

# Convertimos la imagen cargada a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicamos el algoritmo de Canny para la detección de bordes
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Aplicamos la transformación de Hough para detectar líneas
lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)

# Dibujamos las líneas detectadas sobre el archivo original
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Mostramos en pantalla la imagen resultante
cv2.imshow('Trans. de Hough - Lineas', image)
# Esperamos un enter para cerrar la ventana de vista previa
cv2.waitKey(0)
cv2.destroyAllWindows()
