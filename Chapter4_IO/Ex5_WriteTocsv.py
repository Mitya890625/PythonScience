import numpy as np

f, a, da = np.loadtxt("Ex3.txt", skiprows=5, unpack=True)

np.savetxt('Ex3_new.csv', list(zip(f, a, da)),
           fmt="%0.16e", delimiter=",")