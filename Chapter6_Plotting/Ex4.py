import numpy as np
import matplotlib.pyplot as plt


tdata, ydata, dydata =np.loadtxt('Ex4_data.txt', skiprows=4, unpack =True)
t = np.linspace(0, 45, 128)
y = (3.0 +(0.5*np.sin((np.pi*t)/5)))*t*np.exp(-t/10)
plt.errorbar(tdata,ydata, yerr=dydata,zorder=1)
plt.plot(t,y, zorder=0)
plt.xlabel('time, sec')
plt.ylabel('position, cm')
plt.legend(loc='upper right', title='legend')
plt.axhline(color='grey', zorder=-1)
plt.axvline(color='grey', zorder=-1)
plt.show()    