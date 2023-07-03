# Importamos las librerías necesarias
import cv2
import numpy as np

# Cargamos una imagen de entrada a color
image = cv2.imread('entrada_circulo.png', cv2.IMREAD_COLOR)
# Convertimos la imagen cargada a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicamos el algoritmo de Canny para la detección de bordes
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Aplicamos la transformación de Hough para detectar círculos
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=10, minDist=150,
                           param1=50, param2=30, minRadius=10, maxRadius=100)

# Dibujamos los círculos detectados sobre la imagen original y el centro del mismo
if circles is not None:
    circles = np.uint16(np.around(circles))  
    for pt in circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
        cv2.circle(image, (a, b), r, (0, 255, 0), 2) 
        #Imprimimos en consola la ubicación del centro de la circunferencia
        print("Centro ({:}, {:}), radio = {:}".format(a, b, r))
        cv2.circle(image, (a, b), 1, (0, 0, 255), 3)

# Mostramos en pantalla la imagen resultante
cv2.imshow('Trans. de Hough - Circulos', image)
# Esperamos un enter para cerrar la ventana de vista previa
cv2.waitKey(0)
cv2.destroyAllWindows()
