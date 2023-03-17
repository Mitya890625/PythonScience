import numpy as np
def find_V(V0, a, z):
    V = V0*(1 - (z/np.sqrt(a**2+z**2)))
    print(V)
def main():
    find_V(10, 2.5, 13)
main()