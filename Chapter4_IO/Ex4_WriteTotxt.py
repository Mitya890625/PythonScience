import numpy as np

f, a, da = np.loadtxt("Ex3.txt", skiprows=5, unpack=True)

np.savetxt("Ex3_new.txt", list(zip(f, a, da)), fmt="%0.1f",
delimiter=" ", newline=" \n", header="Data_10_03_2023",
footer="", comments="#")
