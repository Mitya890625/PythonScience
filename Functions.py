# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:49:35 2022

@author: LAPTOP-VQE49TEL
"""

import numpy as np
import matplotlib.pyplot as plt
from random import *
def main():
    '''
    a=10
    x = np.linspace(0, 20, 255)
    j0 = first_bessel_func(x)
    j1 = first_bessel_func(x)/x-np.cos(x)/x
    j2 = (3*sec_bessel_func(x)-first_bessel_func(x))/2
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(x, j0)
    ax.plot(x, j1, ':')
    ax.plot(x, j2, '--')
    ax.set_xlim(0, 20)
    ax.axhline(color="grey", zorder=-1)
    fig.show()
    '''
    #simulate_rolling_dice()
    integral()
    
   
def first_bessel_func (x):
    y=[]
    for xx in x:
        if xx == 0.0:
            y+=[1]
        else:
            y+=[np.sin(xx)/xx]
    return np.array(y)
            
    
def sec_bessel_func(x):
    y=[]
    for xx in x:
        if xx == 0.0:
            y+=[1]
        else:
            y+=[np.sin(xx)/(xx*xx) - np.cos(xx)/xx]
    return np.array(y)
    
    
def third_bessel_func(x):
    y=[]
    a = 3
    for xx in x:
        if xx == 0.0:
            y+=[1]
        else:
            y+=[(((3/xx**2)-1)*(np.sin(xx)/a))-(3*np.cos(xx))/xx**2]
    return np.array(y)
def simulate_rolling_dice():
    sum = 0
    dice_1 = []
    dice_2 = []
    sum_arr = []
    for i in range(100):
        rnum = randint(1,7)
        dice_1.append(rnum)
    for j in range(100):
        rnum = randint(1,7)
        dice_2.append(rnum)
    for k in range(100):
        sum = dice_1[k] + dice_2[k]
        sum_arr.append(sum)  
    
    plt.hist(sum_arr, 100, histtype='stepfilled')        
    plt.show()
    
def integral():
    f = lambda x: np.sinc(x)
    a = 0
    b = 5
    n = 100
    h = (b-a)/n
    S = 0.5 * (f(b)+f(a))
    for i in range(1, n):
        S +=f(a+i*h)
    I = h * S
    print(I)
    
    
    
    

main()