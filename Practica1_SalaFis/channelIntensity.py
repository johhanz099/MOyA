import cv2
import numpy as np

# Carga imagen
imagen = cv2.imread("Rainbow.jpg")

#x = input("Ingrese coordenada x: ") 964
#y = input("Ingrese coordenada y: ") 775

# Coordenadas en la imagen
x = 400
y = 358

# Acceder a los píxeles del canal
pixel_b = imagen[y, x, 0]  # Azul
pixel_g = imagen[y, x, 1]  # Verde
pixel_r = imagen[y, x, 2]  # Rojo

# Crear un array con las intensidades
intensidad_pixel = np.stack([pixel_r, pixel_g, pixel_b], axis=0)
print(f"Intensidades del pixel [R G B] en las coordenadas ({x}, {y}): {intensidad_pixel}")
