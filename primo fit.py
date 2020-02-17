import numpy as np
import matplotlib as mlpt
import matplotlib.pyplot as plt
import pylab as py
from matplotlib.widgets import Slider, Button, RadioButtons

f, vin, vout=np.loadtxt('filtro dati di merda.txt', unpack=True)

g=vout/vin

c2=1e-7
c1=1e-5
r1=330
r2=330

ff=np.logspace(-1,6,1000)
ww=2*np.pi*ff

G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
fi=np.arctan(G.imag/G.real)

plt.figure(1)
#curva
plt.loglog(ff, mod, color='blue')

#dati
plt.errorbar(f, g, 0, 0.05*f, ls='', color='red', marker='o')
plt.show()

