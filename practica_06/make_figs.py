import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-dark') 
# El estilo 'science' requiere instalar matplotlib-scientific-style.
# python -m pip install --user seaborn

def make_fig(I_ref,name_data,name_fig,xerr_,err_var,label_):

    # for p1,p2,p3 with varible error = True
    if err_var:
        data = np.genfromtxt(name_data,delimiter=None,skip_header=1)
        R = data[:,0]/I_ref*100
        err_y = data[:,1]
        deg = data[:,2]
        plt.errorbar(
        deg, R, xerr=xerr_, yerr=err_y/I_ref*100,
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
        plt.title(r"Reflectancia vs Ángulo $\theta$ - "+label_)
    # for p4 with variable error = False
    else:
        data = np.genfromtxt(name_data,delimiter=None,skip_header=1)
        R = data[:,0]/I_ref*100
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
        plt.title(r"Reflectancia vs Ángulo $\theta$ - "+label_)
    
    # for both
    plt.xlabel(r"$\theta (^{\circ})$")
    plt.ylabel(r"Reflectancia ($\%$)")
    plt.grid()
    plt.legend()
    plt.savefig(name_fig)
    plt.close()

# dir names
fig = "fig/"
dat = "data/"
# Make figs
make_fig(729,dat+"p1_noPol.txt",fig+"p1_noPol.pdf",2.5,True,r"Luz natural")
make_fig(336,dat+"p2_0deg.txt",fig+"p2_0deg.pdf",2.5,True,r"Polarización $s$")
make_fig(289,dat+"p3_90deg.txt",fig+"p3_90deg.pdf",2.5,True,r"Polarización $p$")
#make_fig(1200,dat+"p4_30deg.txt",fig+"p4_30deg.pdf",2.5,False,r"Para $\theta_i = 30^{\circ}$")
#make_fig(1200,dat+"p4_70deg.txt",fig+"p4_70deg.pdf",2.5,False,r"Para $\theta_i = 70^{\circ}$")



