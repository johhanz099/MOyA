import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.style.use('seaborn-v0_8-dark') 

# Import data
dat_dir = "data/"
out_fig = "fig/"
data_30 = np.genfromtxt(dat_dir+"p4_30deg.txt",delimiter=None,skip_header=1)
data_70 = np.genfromtxt(dat_dir+"p4_70deg.txt",delimiter=None,skip_header=1)

# Define variables
R_30 = data_30[:,0]
d_30 = data_30[:,1]
R_70 = data_70[:,0]
d_70 = data_70[:,1]

# Def function
def malus(phi, I0, phi0):
    return I0 * np.cos(np.radians(phi - phi0))**2

# Fit
popt_30, pcov_30 = curve_fit(malus, d_30, R_30, p0=[60, 45])
popt_70, pcov_70 = curve_fit(malus, d_70, R_70, p0=[60, 45])
I0_30, phi0_30 = popt_30
I0_70, phi0_70 = popt_70
dI0_30, dphi0_30 = np.sqrt(np.diag(pcov_30))
dI0_70, dphi0_70 = np.sqrt(np.diag(pcov_70))

# Cálculo de R^2 for 30 deg
residuals = R_30 - malus(d_30, *popt_30)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((R_30 - np.mean(R_30))**2)
r_squared_30 = 1 - (ss_res / ss_tot)
# Cálculo de R^2 for70 deg
residuals_ = R_70 - malus(d_70, *popt_70)
ss_res_ = np.sum(residuals**2)
ss_tot_ = np.sum((R_30 - np.mean(R_30))**2)
r_squared_70 = 1 - (ss_res_ / ss_tot_)

# Plot fit
phi_fit = np.linspace(0, 350, 500)
fit_30 = malus(phi_fit, *popt_30)
fit_70 = malus(phi_fit, *popt_70)

# Plot for 30
plt.figure(figsize=(8, 5))
plt.plot(d_30, R_30, 'o', label='Datos experimentales (30°)')
plt.plot(phi_fit, fit_30, '-', label=(
    f'Ajuste $I = I_0 \cos(\phi - \phi_0)$\n'
    f'$I_0 = {I0_30:.1f} \\pm {dI0_30:.1f}$\n'
    f'$\\phi_0 = {phi0_30:.1f}^\\circ \\pm {dphi0_30:.1f}^\\circ$\n'
    f'$R^2 = {r_squared_30:.4f}$'))
plt.xlabel('Ángulo del analizador (°)')
plt.ylabel('Intensidad')
plt.title('Ley de Malus - Incidencia de 30°')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(out_fig+"p4_30deg.pdf")
plt.close()


# Plot for 70
plt.figure(figsize=(8, 5))
plt.plot(d_70, R_70, 'o', label='Datos experimentales (70°)')
plt.plot(phi_fit, fit_70, '-', label=(
    f'Ajuste $I = I_0 \cos(\phi - \phi_0)$\n'
    f'$I_0 = {I0_70:.1f} \\pm {dI0_70:.1f}$\n'
    f'$\\phi_0 = {phi0_70:.1f}^\\circ \\pm {dphi0_70:.1f}^\\circ$\n'
    f'$R^2 = {r_squared_70:.4f}$'))
plt.xlabel('Ángulo del analizador (°)')
plt.ylabel('Intensidad')
plt.title('Ley de Malus - Incidencia de 70°')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(out_fig+"p4_70deg.pdf")
plt.close()