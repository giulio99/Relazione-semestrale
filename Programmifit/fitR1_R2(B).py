import numpy as np
import matplotlib as mlpt
import matplotlib.pyplot as plt
import pylab as py 
from scipy.optimize import curve_fit

f, df, vin, dvin, vout, dvout=np.loadtxt('R1_uguale_R2.txt', unpack=True)

g=vout/vin
dg=np.sqrt(((1/vin)*dvout)**2+((vout*dvout)/(vin**2))**2)

c2=1e-7
c1=1e-5
r1=330
r2=330

ff=np.logspace(-1,6,1000)
ww=2*np.pi*ff

G=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
fi=np.arctan(G.imag/G.real)


#curva
#plt.loglog(ff, mod, color='blue')
#plt.errorbar(f, g, dg, 0.05*f, ls='', color='red', marker='o')

##FIT

def funz(f, r1, r2,c1,c2):
    ww=f*2*np.pi
    h=r1*r2*c1*c2
    t=(1+ww*1j*c2*(r1+r2)+((1j*ww)**2)*h)/(1+ww*1j*c2*(r1*(1+c1/c2)+r2)+((1j*ww)**2)*h)
    return np.sqrt((t.real)**2+(t.imag)**2)
    
init=(329,329,1e-7,1e-5)

pars, covm = curve_fit(funz,f , g, init, dg, absolute_sigma=False) 
w0=1/(2*np.pi*np.sqrt((pars[0]*pars[1]*pars[2]*pars[3])))
#w0=np.sqrt(1/pars[4])
print('w0= %f'%w0)
#print('Parametri iniziali:\n', pars)
#print('Matrice di covarianza:\n', covm)
print('R1= %f +- %f ' %(pars[0],np.sqrt(covm[0][0])))
print('R2= %f +- %f ' %(pars[1],np.sqrt(covm[1][1])))
print('C1= %f +- %f ' %(pars[2],np.sqrt(covm[2][2])))
print('C2= %f +- %f ' %(pars[3],np.sqrt(covm[3][3])))

plt.figure(1)
plt.title('Guadagno filtro R1=R2', fontsize=16)
plt.xlabel('Frequenza  [Hz]')
plt.ylabel('Guadagno [u.a.]')
plt.loglog(ff,funz(ff,*pars), color='blue')
plt.errorbar(f, g, dg, 0.05*f, ls='', color='red', marker='.')
plt.grid()
plt.show()

