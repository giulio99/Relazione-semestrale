import numpy as np
import matplotlib as mlpt
import matplotlib.pyplot as plt
import pylab as py
from matplotlib.widgets import Slider, Button, RadioButtons

f, df, Vin, dVin, Vout, dVout=np.loadtxt('passabanda(r1=r2)(con errore).txt', unpack=True)

g=Vout/Vin

c1=0.47e-6
c2=4.7e-6
r1=330
r2=330

ff=np.logspace(-1,6,1000)
ww=2*np.pi*ff

G=-(1+1j*ww*r1*(c1+c2)+((1j*ww)**2)*r1*r2*c1*c2)/(1+1j*ww*r1*(c2*(1+r1/r2)+c1)+((1j*ww)**2)*r1*r2*c1*c2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
fi=np.arctan(G.imag/G.real)

plt.figure(1)
#curva
plt.loglog(ff, mod, color='blue')

#dati
plt.errorbar(f, g, 0, 0.05*f, ls='', color='red', marker='o')
plt.show()