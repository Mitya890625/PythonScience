import numpy as np
import matplotlib.pyplot as plt

x3 = np.linspace(-np.pi, np.pi, 150)
y3c = np.cos(x3)
y3s = np.sin(x3)
plt.plot(x3,y3c, 'green', label='Cos(x)')
plt.plot(x3,y3s, 'orange', label='Sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left', title='legend')
plt.axhline(color='grey', zorder=-0.5)
plt.axvline(color='grey', zorder=-0.5)
plt.show()

