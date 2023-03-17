import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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


def dsdt(t, S):
    x, y, z = S
    a = 40
    b = 5
    c = 35
    return[a*(y-x),
           (c-a)*x-x*z+c*y,
           x*y-b*z]