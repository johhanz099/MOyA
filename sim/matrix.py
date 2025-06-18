import numpy as np
import matplotlib.pylab as plt

size = 1025 # Tamaño de la matriz
size_m = int(size/2) # Tamaño desde el origen al lado
lado = 5 #lado en cm
step_cm = lado/size # paso
coord = np.linspace(-lado/2,lado/2,size)
#coord_z = np.arange(-size_m,size_m+1)
#coord_y = coord_z

z,y = np.meshgrid(coord,coord)

#print(coord)
#print(x)
#print("salto en *x* y *y*=",step_cm)
#print("Distancia total =",step_cm*size)

# Def vec r con altura x
r_x = 100 # cm

# Constantes
a = 0.000025e-1 # parametro (cm)
i_0 = 250 # intensidad base (u.a)
long_onda = 532e-6 #  longitud de onda en cm RARO

# Puntos
s1 = a/2
s2 = -a/2

# Distancias
d_s1 = np.sqrt((s1-z)**2 + (r_x)**2 + y**2)
d_s2 = np.sqrt((s2-z)**2 + (r_x)**2 + y**2)

#print("distancia (cm) s1:",d_s1)
#print("distancia (cm) s2:",d_s2)

# Calcular Int_r
Int_1 = i_0/d_s1**2
Int_2 = i_0/d_s2**2
Int_r = Int_1 + Int_2 + 2*np.sqrt(Int_1*Int_2)*np.cos(2*np.pi*(d_s2-d_s1)/long_onda)

plt.imshow(Int_r)
plt.xlabel("y")
plt.ylabel("x")
plt.colorbar()
plt.savefig('fig.pdf')