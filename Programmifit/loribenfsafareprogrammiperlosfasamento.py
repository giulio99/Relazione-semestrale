import numpy as np
import matplotlib as mlpt
import matplotlib.pyplot as plt
import pylab as py
from scipy.optimize import curve_fit

f,df,T=np.loadtxt('sfasamento.txt', unpack=True)

dt=T*0.08

P=-2*np.pi*f*T

dP=np.sqrt((2*np.pi*f*dt)**2+(2*np.pi*T*df))

ff=np.logspace(0,5.2,1000)
ww=2*np.pi*ff

c2=1e-7
c1=1e-5
r1=330
r2=330

G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
fi=np.arctan(G.imag/G.real)

plt.figure(1)
plt.title('Grafico dello sfasamento tra Vin e Vout', fontsize='16')
plt.ylabel('Sfasamento [rad]')
plt.xlabel('Frequenza  [Hz]')
plt.semilogx(ff,fi, color='blue')
plt.errorbar(f, P,dP, df, ls='', color='red', marker='.', label='\nR1=R2=330 $\Omega$\nC1=10 $\mu$F C2=0.1 $\mu$F')
plt.legend(loc='lower right')
plt.grid()
plt.show()
