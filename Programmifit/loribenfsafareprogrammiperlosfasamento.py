import numpy as np
import matplotlib as mlpt
import matplotlib.pyplot as plt
import pylab as py
from scipy.optimize import curve_fit

f,dT=np.loadtxt('sfasamento.txt', unpack=True)
DP=-2*np.pi*f*dT

ff=np.logspace(0,5,1000)
ww=2*np.pi*ff

c2=1e-7
c1=1e-5
r1=330
r2=330




G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
fi=np.arctan(G.imag/G.real)

plt.semilogx(ff,fi, color='blue')
plt.errorbar(f, DP, ls='', color='red', marker='.')
plt.grid()
plt.show()