import numpy as np
import cv2
import matplotlib.pyplot as plt

# Ruta al video
VIDEO_PATH = 'Mejor.mp4'  # <- cambia esto por el nombre real del archivo

# Coordenadas de los 6 puntos que deseas seguir (x, y)
# REEMPLAZA ESTAS COORDENADAS CON LAS QUE TÚ ELIJAS
puntos = [
    (120, 150),
    (200, 160),
    (250, 180),
    (300, 190),
    (350, 200),
    (400, 210)
]

# === CARGA DEL VIDEO Y PRIMER FRAME ===
cap = cv2.VideoCapture(VIDEO_PATH)
ret, frame = cap.read()
cap.release()

if not ret:
    print("No se pudo leer el video.")
    exit()
    
# Convertir BGR (OpenCV) a RGB (matplotlib)
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Dibujar los puntos sobre la imagen
fig, ax = plt.subplots(figsize=(8, 6))
ax.imshow(frame_rgb)
for i, (x, y) in enumerate(puntos):
    ax.plot(x, y, 'go')  # 'go' = green circle
    ax.text(x + 5, y, f'{i+1}', color='green', fontsize=10)

ax.set_title("Puntos seleccionados en el primer fotograma")
plt.axis('off')
plt.tight_layout()
plt.show()