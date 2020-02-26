import numpy as np
import matplotlib as mlpt
import matplotlib.pyplot as plt
import pylab as py 
from scipy.optimize import curve_fit

##1
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
plt.suptitle('Simulazione guadagno filtro', fontsize=16)

plt.subplot(4, 2, 1)
plt.loglog(ff, mod, color='blue', label="R1=330 Hz, R2=330 Hz")
plt.legend(loc = 'upper right')
plt.grid()

##2
r1=33
r2=330
G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)

plt.subplot(4, 2, 2)
plt.loglog(ff, mod, color='blue', label="R1=33 Hz, R2=330 Hz")
plt.legend(loc = 'upper right')
plt.grid()

##3
r1=330
r2=33
G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
plt.subplot(4, 2, 3)
plt.loglog(ff, mod, color='blue', label="R1=330 Hz, R2=33 Hz")
plt.legend(loc = 'upper right')
plt.grid()

##4
r1=3300
r2=330
G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
plt.subplot(4, 2, 4)
plt.loglog(ff, mod, color='blue', label="R1=3300 Hz, R2=330 Hz")
plt.legend(loc = 'upper right')
plt.grid()

##5
r1=330
r2=3300
G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
plt.subplot(4, 2, 5)
plt.loglog(ff, mod, color='blue', label="R1=330 Hz, R2=3300 Hz")
plt.legend(loc = 'upper right')
plt.grid()


##6
r1=33000
r2=330
G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
plt.subplot(4, 2, 6)
plt.loglog(ff, mod, color='blue', label="R1=33000 Hz, R2=330 Hz")
plt.legend(loc = 'upper right')
plt.grid()

##7
r1=330
r2=33000
G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
plt.subplot(4, 2, 7)
plt.loglog(ff, mod, color='blue', label="R1=330 Hz, R2=33000 Hz")
plt.legend(loc = 'upper right')
plt.grid()

##8
r1=33000
r2=33000
G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
plt.subplot(4, 2, 8)
plt.loglog(ff, mod, color='blue', label="R1=33000 Hz, R2=33000 Hz")
plt.legend(loc = 'upper right')
plt.grid()


fig=plt.figure(1)
fig.subplots_adjust(hspace=0)
fig.add_subplot(111, frameon=False)
plt.xlabel('Frequenza  [Hz]')
plt.ylabel('Guadagno [u.a.]')
plt.show()





















