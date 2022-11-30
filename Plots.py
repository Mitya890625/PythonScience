# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:55:58 2022

@author: LAPTOP-VQE49TEL
"""

import numpy as np
import matplotlib.pyplot as plt
#issue1

def main():
    x1 =np.linspace(-1, 3, 20)
    y1 =3*(x1**2)
    x2 = np.linspace(-15, 15, 150)
    y2 = np.cos(x2)/(1+(0.2*x2**2))
    x3 = np.linspace(-np.pi, np.pi, 30)
    y3c = np.cos(x3)
    y3s = np.sin(x3)
    x5 = np.random.randn(20)
    y5 = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*x5**2)
    #plot_tripleXSquared(x1,y1)
    #plot_issue2(x2,y2)
    #plot_issue3(x3, y3c, y3s)
    #plot_issue4(tdata, ydata, dydata)
    #plot_issue5(x5)
    x = np.linspace(-2.6*np.pi, 2.6*np.pi, 200)
    y = np.sqrt((8./x)**2-1.)
    tan = np.tan(x)
    ytanM = np.ma.masked_where(np.abs(tan) > 20., tan)
    cot = 1.0/tan
    ycotM = np.ma.masked_where(np.abs(cot) > 20., cot)
    plt.rc('mathtext', fontset='stix')
    fig, ax = plt.subplots(2,1, figsize=(8,6), sharex=True, sharey=True)
    ax[0].plot(x, ytanM)
    ax[0].plot(x,y, linestyle=':')
    ax[1].plot(x, ycotM)
    ax[1].plot(x,-y, linestyle=':')
    ax[0].set_xlim(0, 8)
    ax[0].set_ylim(-7.5, 7.5)
    ax[0].set_ylabel(r'$\tan\theta$')
    ax[1].set_xlabel(r'$\theta$')
    ax[1].set_ylabel(r'$\cot\theta$')
    for i in range(2):
        ax[i].axhline(color='gray', zorder=-1)
        
   
    fig.show()
'''
x = np.linspace(-2*np.pi, 2*np.pi, 200)
sin, cos, tan = np.sin(x), np.cos(x), np.tan(x)
csc, sec, cot = 1.0/sin, 1.0/cos, 1.0/tan

plt.close('all') # Closes all open figure windows
fig, ax = plt.subplots(2, 3, figsize=(9.5, 6),
sharex=True, sharey=True)
ax[0, 0].plot(x, sin, color='red')
ax[0, 1].plot(x, cos, color='orange')
ax[0, 2].plot(x, np.ma.masked_where(np.abs(tan) > 20., tan),
color='yellow')
ax[1, 0].plot(x, np.ma.masked_where(np.abs(csc) > 20., csc),
color='green')
ax[1, 1].plot(x, np.ma.masked_where(np.abs(sec) > 20., sec),
color='blue')
ax[1, 2].plot(x, np.ma.masked_where(np.abs(cot) > 20., cot),
color='violet')
ax[0, 0].set_xlim(-2*np.pi, 2*np.pi)
ax[0, 0].set_ylim(-5, 5)
ax[0, 0].set_xticks(np.pi*np.array([-2, -1, 0, 1, 2]))
ax[0, 0].set_xticklabels(['-2$\pi$', '-$\pi$', '0',
 '$\pi$', '2$\pi$'])

ax[0, 2].patch.set_facecolor('lightgray')

ylab = [['sin', 'cos', 'tan'], ['csc', 'sec', 'cot']]
for i in range(2):
    for j in range(3):
     ax[i, j].axhline(color='gray', zorder=-1)
     ax[i, j].set_ylabel(ylab[i][j])

fig.savefig('figures/multiplePlotsGrid.pdf')
fig.show()
fig.canvas.manager.window.raise_() 
'''
'''
    tdata, ydata, dydata =np.loadtxt('Issue6_4.txt',skiprows=4, unpack =True)
    t = np.linspace(0, 45, 128)
    y = (3.0 +(0.5*np.sin((np.pi*t)/5)))*t*np.exp(-t/10)
    #Udata, Idata = np.loadtxt('DiodePlot.txt', skiprows=1, unpack=True)
    plt.errorbar(tdata,ydata, yerr=dydata,zorder=1)
    plt.plot(t,y, zorder=0)
    plt.xlabel('time (s)')
    plt.ylabel('position (cm)')
    plt.legend(loc='upper right', title='legend')
    plt.axhline(color='grey', zorder=-1)
    plt.axvline(color='grey', zorder=-1)
    plt.show()    
'''
    x = np.linspace(-400, 0.1, 100)
    y0, e, T, k = 1, 1.6*10**-19, 300, 1.38*10**-23
    y = y0*(np.exp((e*x)/(k*T))-1)
    plt.semilogy(x,y, zorder=0)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    #plt.legend(loc='center', title='legend')
    plt.axhline(color='grey', zorder=-1)
    plt.axvline(color='grey', zorder=-1)
    plt.show()    
    '''
def plot_tripleXSquared(x,y):
    plt.plot(x,y, 'r-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(zorder=-1)
    plt.axvline(zorder=-1)
    plt.show()
def plot_issue2(x,y):
    plt.plot(x,y, 'r-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(zorder=-1)
    plt.axvline(zorder=-1)
    plt.show()
def plot_issue3(x,y,z):
    plt.plot(x,y, 'green', label='Cos(x)')
    plt.plot(x,z, 'orange', label='Sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper left', title='legend')
    plt.axhline(color='grey', zorder=-1)
    plt.axvline(color='grey', zorder=-1)
    plt.show()
def plot_issue5(x):
    plt.hist(x)
   
    
    
     

main()   
     
 