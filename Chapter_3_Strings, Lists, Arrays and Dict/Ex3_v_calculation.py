import numpy as np

g, h0 = 9.8, 10
y = np.arange(10, 0, -0.5)
print(y)
t = np.sqrt((2*(h0-y))/g)
print(t)
