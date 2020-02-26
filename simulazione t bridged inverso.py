import numpy as np
import matplotlib as mlpt
import matplotlib.pyplot as plt
import pylab as py
from matplotlib.widgets import Slider, Button, RadioButtons


f,df, vin,dvin, vout,dvuot=np.loadtxt('circuito inverso.txt', unpack=True)

g=vout/vin


fig, ax=plt.subplots()
plt.subplots_adjust( bottom=0.4)
ff=np.logspace(-6,6,1000)
ww=2*np.pi*ff

c2=1e-7
c1=1e-5
r1=330
r2=330

G=-1*(1+ww*1j*r1*(c1+c2)+((1j*ww)**2)*c1*c2*r1*r2)/(1+ww*1j*r1*(c2*(1+(r2/r1))+c1)+((1j*ww)**2)*c1*c2*r1*r2)
mod=np.sqrt((G.real)**2+(G.imag)**2)
fi=np.arctan(G.imag/G.real)

l, =plt.loglog(ff, mod)
plt.errorbar(f, g, 0, 0.05*f, ls='', color='red', marker='o')

axcolor = 'lightgoldenrodyellow'
axc2 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axc1 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axr2 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
axr1 = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)

sc2 = Slider(axc2, 'c2', 1e-7, 1e-4, valinit=c2)
sc1 = Slider(axc1, 'c1', 1e-7, 1e-5, valinit=c1)
sr2 = Slider(axr2, 'r2', 33, 330000, valinit=r2, valstep=10)
sr1 = Slider(axr1, 'r1', 33, 330000, valinit=r1, valstep=10)

def update(val):
    valc1 = sc1.val
    valc2 = sc2.val
    valr1 = sr1.val
    valr2 = sr2.val
    val=(-1*(1+ww*1j*valr1*(valc1+valc2)+((1j*ww)**2)*valc1*valc2*valr1*valr2)/(1+ww*1j*valr1*(valc2*(1+(valr2/valr1))+valc1)+((1j*ww)**2)*valc1*valc2*valr1*valr2))
    l.set_ydata(np.sqrt((val.real)**2+(val.imag)**2))
    fig.canvas.draw_idle()

sc1.on_changed(update)
sc2.on_changed(update)
sr1.on_changed(update)
sr2.on_changed(update)


resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sc1.reset()
    sc2.reset()
    sr1.reset()
    sr2.reset()
button.on_clicked(reset)

resetax = plt.axes([0.25, 0.025, 0.1, 0.04])
stamp = Button(resetax, 'stampa', color=axcolor, hovercolor='0.975')

def stampa(event):
    print(sr1.val)
    print(sr2.val)
    print(sc1.val)
    print(sc2.val)

stamp.on_clicked(stampa)

plt.show()











