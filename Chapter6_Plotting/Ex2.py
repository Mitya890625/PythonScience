import numpy as np
import matplotlib.pyplot as plt

x2 = np.linspace(-15, 15, 150)
y2 = np.cos(x2)/(1+(0.2*x2**2))
plt.plot(x2, y2, 'r-')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(color='gray', zorder=-1)
plt.axvline(color='gray', zorder=-1)
plt.show()