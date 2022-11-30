# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 11:52:08 2022

@author: LAPTOP-VQE49TEL
"""

import numpy as np
import scipy.linalg as sclin
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def main():
    #linear_equation()
    #integration()
    x0 = -10
    y0 = 0
    z0 = 35
    S0 = (x0, y0, z0)
    t = np.arange(0., 25, 0.05)
    sol = odeint(dsdt, S0, t, tfirst=True)
    xsol = sol.T[0]
    ysol = sol.T[1]
    zsol = sol.T[2]
    fig, ax = plt.subplots(3,1, figsize=(20,16))
    ax[0].plot(ysol, xsol, dashes=(1,2), ms=1, color='black')
    ax[1].plot(zsol, ysol, dashes=(1,2), ms=1, color='black')
    ax[2].plot(xsol, zsol, dashes=(1,2), ms=1, color='black')
    fig.show
    
    

def linear_equation():
    A = [[1,-2, 9, 13], [-5,1,6,-7], [4,8,-4,-2], [8,5,-7,1]]
    b = [1,-3,-2,5]
    sol = sclin.solve(A,b)
    print(sol)
    
def integration():
    print(quad(lambda x: (1/(1+x**2)), -1, 1))
    print(quad(lambda x: (1/((np.exp(x)+x+1)**2+(np.pi)**2)), -np.inf, np.inf))
def dsdt(t, S):
    x, y, z = S
    a = 40
    b = 5
    c = 35
    return[a*(y-x),
           (c-a)*x-x*z+c*y,
           x*y-b*z]
    
    
    
    
main()