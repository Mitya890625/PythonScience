import numpy as np

g, h0 = 9.8, 10
y = np.arange(10, 0, -0.5)
print(y)
t = np.sqrt((2*(h0-y))/g)
print(t)
delta_v = (y[1:]-y[:-1])/(t[1:]-t[:-1])
delta_t = t[1:]-t[:-1]
print(delta_v)
delta_a = (delta_v[1:] - delta_v[:-1]) / (delta_t[1:] - delta_t[:-1])
print(delta_a)