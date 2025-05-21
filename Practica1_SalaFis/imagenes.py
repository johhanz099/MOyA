import cv2
import numpy as np

# Cargar las imágenes en escala de grises (rojo, verde, azul)
imagen_azul = cv2.imread("P01_Blue.jpg", cv2.IMREAD_GRAYSCALE)
imagen_verde = cv2.imread("P01_Green.jpg", cv2.IMREAD_GRAYSCALE)
imagen_roja = cv2.imread("P01_Red.jpg", cv2.IMREAD_GRAYSCALE)

# Verificar si las imágenes se cargaron correctamente
if imagen_roja is None or imagen_verde is None or imagen_azul is None:
    print("Error: No se pudieron cargar las imágenes.")
    exit()

# Combinar las imágenes en una imagen RGB
imagen_rgb = cv2.merge((imagen_azul, imagen_verde, imagen_roja))

# Mostrar la imagen RGB (opcional)
cv2.imshow("Imagen RGB", imagen_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar la imagen RGB (opcional)
cv2.imwrite("imagen_rgb.png", imagen_rgb)