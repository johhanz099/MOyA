import cv2
import numpy as np

# Cargar una imagen en color
img = cv2.imread('Rainbow.jpg')

# Dividir la imagen en canales
b, g, r = cv2.split(img)


# Guardar las imagenes para cada canal
cv2.imwrite("imagen_r.jpg", r)
cv2.imwrite("imagen_g.jpg", g)
cv2.imwrite("imagen_b.jpg", b)