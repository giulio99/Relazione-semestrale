import numpy as np
import matplotlib as mlpt
import matplotlib.pyplot as plt
import pylab as py
from matplotlib.widgets import Slider, Button, RadioButtons

f,df, vin, dvin, vout, dvout=np.loadtxt('R1=R2.txt', unpack=True)

g=vout/vin
dg=np.sqrt((((1/vin)*dvout)**2)+((vout/(vin**2))*dvin)**2)
c2=1e-7
c1=1e-5
r1=330
r2=330

ff=np.logspace(-1,6,1000)
ww=2*np.pi*ff

G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
def fit(f):
    ww=f*2*np.pi
    G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
    return np.sqrt((G.real)**2+(G.imag)**2)

mod=np.sqrt((G.real)**2+(G.imag)**2)
fi=np.arctan(G.imag/G.real)

plt.figure(1)
#curva
plt.loglog(ff, mod, color='blue')

#dati
plt.errorbar(f, g, dg, df, ls='', color='red', marker='o')
chisq = sum(((g-fit(f))/dg)**2) #Chiquadro
print('Chiquadro= %f' %(chisq))
#dati

plt.show()

