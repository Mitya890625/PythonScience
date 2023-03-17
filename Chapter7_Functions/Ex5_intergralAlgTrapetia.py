import numpy as np

def integral():
    f = lambda x: np.exp(-1*(x**2))
    a = 0
    b = 3.5
    n = 1000000
    h = (b-a)/n
    S = 0.5 * (f(b)+f(a))
    for i in range(1, n):
        S +=f(a+i*h)
    I = h * S
    print(I)
    
integral()