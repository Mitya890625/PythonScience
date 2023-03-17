import numpy as np
import matplotlib.pyplot as plt

x1 =np.linspace(-1, 3, 100)
y1 =3*(x1**2)
plt.plot(x1, y1)
plt.xlabel('x')
plt.ylabel('y')
plt.show()