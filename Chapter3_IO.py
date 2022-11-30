# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:21:46 2022

@author: LAPTOP-VQE49TEL
"""

import numpy as np
import numpy
import matplotlib.pyplot as plt
'''
total_amount_of_money = float(input("How much money (in dollars) in your launch account"))
current_day = float(input("What day of the month is today?"))
number_of_days = float(input("How many days in this month?"))
daily_allowance = total_amount_of_money / (number_of_days - current_day)
#print("You can spend ${0:0.3f} each day for the rest of the month".format(daily_allowance))
np.loadtxt()
'''
#Writing into file&Saving into file


'''
f, a, da = np.loadtxt("Issue3_3.txt", skiprows=5, unpack=True)




np.savetxt("Chapter3Problem4.txt", list(zip(f, a, da)), fmt="%0.1f",
delimiter=" ", newline=" \n", header="Data_25_05_2022",
footer="", comments="#")

np.savetxt('Chapter3Problem4.csv', list(zip(f, a, da)),
           fmt="%0.3f", delimiter=",")
'''
U, I = np.loadtxt('F0Diod.csv', skiprows=3,
                          unpack=True, delimiter=",")
plt.plot(U,I)
plt.show()