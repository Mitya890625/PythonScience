import numpy as np

f, a, da = np.loadtxt("Ex3.txt", skiprows=5, unpack=True)

'''
np.savetxt("Ex3.txt", list(zip(f, a, da)), fmt="%0.4f",
delimiter=" ", newline=" \n", header="Data_25_05_2022",
footer="", comments="#")
'''