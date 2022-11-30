# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:46:45 2022

@author: LAPTOP-VQE49TEL
"""

import numpy as np

#b = np.linspace(0, 10, 10)
#print(b) 

#issue 3
g, h0 = 9.8, 10
y = np.arange(10, 0, -0.5)
#print(y)
t = np.sqrt((2*(h0-y))/g)
#print(t)
delta_v = (y[1:]-y[:-1])/(t[1:]-t[:-1])
#print(delta_v)
a_box = np.zeros((8,8), dtype=int)
a_box[0,:] = 1
a_box[:,0] = 1
a_box[7,:] = 1
a_box[:,7] = 1
#print(a_box)
b_checkerboard = np.zeros((8,8), dtype=int)
b_checkerboard[1::2,::2] = 1
b_checkerboard[::2,1::2] = 1
#print(b_checkerboard)
c = np.arange(2, 50, 5)
#print(c) 
c[c%3!=0] = -c[c%3!=0]
print(b_checkerboard.size)
print(b_checkerboard.shape)
print(b_checkerboard.mean())
print(b_checkerboard.std())
print(c.size)
print(c.shape)
print(c.mean())
print(c.std())


