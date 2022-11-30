# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:35:11 2022

@author: LAPTOP-VQE49TEL
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
fig1 = plt.figure()
fig2 = plt.figure()
ax0 = fig.gca(projection='3d')
ax1 = fig1.gca(projection='3d')
ax2 = fig2.gca(projection='3d')

u,v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax0.plot_surface(x,y,z, color='g', alpha=0.3)
ax1.plot_wireframe(x,y,z, color='r', alpha=1)
ax2.contour3D(x,y,z, 20, cmap='binary')