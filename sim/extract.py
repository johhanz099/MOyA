import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Muy importante si no hay entorno gráfico
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

x = 10 #mm
lam = 0.000532
lado = 10 #mm

# Cargar imagen (en escala de grises)
img = cv2.imread('FranjasParalelas.tif', cv2.IMREAD_GRAYSCALE)

#plt.imshow(img, cmap='gray')  # Añade cmap para ver en escala de grises
#plt.xlabel("y")
#plt.ylabel("x")
#plt.colorbar()
#plt.show()
#plt.savefig('fig.pdf')

col_img = img[:,0:-1].mean(axis=1) # Promedia todas las columnas para obtener una forma suave 

picos, _ = find_peaks(col_img)
#print(delta_picos)

#plt.plot(col_img_prom,label="promedio")
plt.plot(col_img,label="Promedio completo")
plt.plot(picos,col_img[picos],'rx',label='picos detectados')
plt.legend()
plt.savefig('picos.pdf')

delta_picos = np.diff(picos) #obtenidas las diferencias entre picos
delta_picos = np.mean(delta_picos)

#print(picos)
#print(delta_picos)

scale = lado / len(col_img) # escala en mm/px
delta_picos_mm = delta_picos * scale

# Separación de la rejilla
a = lam * x / delta_picos_mm
a_micras = a*100
print(f'Distancia entre fuentes (a): {a:.4f} mm')
print(f'Distancia entre fuentes (a): {a_micras:.4f} (micro)m')



