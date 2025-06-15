import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.style.use('seaborn-v0_8-dark') 
# El estilo 'science' requiere instalar matplotlib-scientific-style.
# python -m pip install --user seaborn

def make_fig(name_data,name_fig,xerr_):
    data = np.genfromtxt(name_data,delimiter=None,skip_header=1)
    R = data[:,0]
    deg = data[:,1]
    plt.errorbar(
    deg, R, xerr=xerr_, #yerr=1,
    fmt='o',                    # solo puntos (sin línea)
    #color='blue',               # color de los puntos
    #ecolor='gray',              # color de las barras de error
    #elinewidth=1.5,             # grosor de las barras
    capsize=2,                  # tamaño de las "patitas"
    #marker='o',                # marcador: 'o', 's', '^', 'D', etc.
    markersize=3,               # tamaño del marcador
    linestyle='none',           # evita líneas entre puntos
    label="Mediciones"
    )
    plt.title(r"Intensidad vs ángulo $\theta$")
    plt.xlabel(r"$\theta (^{\circ})$")
    plt.ylabel(r"Intensidad ($u.a$)")
    plt.grid()
    plt.legend()
    plt.savefig(name_fig)
    plt.close()

# dir names
fig = "fig/"
dat = "data/"
# Make figs
make_fig(dat+"p1_noPol.txt",fig+"p1_noPol.pdf",2.5)
make_fig(dat+"p2_0deg.txt",fig+"p2_0deg.pdf",2.5)
make_fig(dat+"p3_90deg.txt",fig+"p3_90deg.pdf",2.5)
make_fig(dat+"p4_30deg.txt",fig+"p4_30deg.pdf",2.5)
make_fig(dat+"p4_70deg.txt",fig+"p4_70deg.pdf",2.5)

