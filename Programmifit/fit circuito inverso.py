import numpy as np
import matplotlib as mlpt
import matplotlib.pyplot as plt
import pylab as py
from scipy.optimize import curve_fit

f,df, vin,dvin, vout,dvout=np.loadtxt('circuito inverso.txt', unpack=True)

g=vout/vin
dg=np.sqrt(((1/vin)*dvout)**2+((vout/vin**2)*dvin)**2)

c2=4.7*1e-6
c1=4.7*1e-7
r1=330
r2=330

ff=np.logspace(-1,6,1000)
ww=2*np.pi*ff

G=-1*(1+ww*1j*r1*(c1+c2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*r1*(c2*(1+(r2/r1))+c1)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
fi=np.arctan(G.imag/G.real)

def guadagno(f, a,b,c,d):
    w=f*2*np.pi
    h=a*b*c*d
    t=-1*(1+w*1j*a*(c+d)+((1j*w)**2)*h)/(1+w*1j*a*(d*(1+(b/a))+c)+((1j*w)**2)*h)
    return np.sqrt((t.real)**2+(t.imag)**2)

init=(330,330,c1,c2)


pars, covm=curve_fit(guadagno, f, g, init, dg, absolute_sigma=False)

for i in range(4):
    print(pars[i], '+-', np.sqrt(covm[i][i]))

plt.figure(1)
plt.loglog(ff, mod, color='blue')
plt.errorbar(f, guadagno(f, *pars),dg , df, ls='', color='black', marker='.')
plt.errorbar(f, g, dg, df, ls='', color='red', marker='o')
plt.show()
