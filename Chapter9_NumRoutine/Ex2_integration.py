import numpy as np
from scipy.integrate import quad 


def integration():
    print(quad(lambda x: (1/(1+x**2)), -1, 1))
    print(quad(lambda x: (1/((np.exp(x)+x+1)**2+(np.pi)**2)), -np.inf, np.inf))
    
integration()