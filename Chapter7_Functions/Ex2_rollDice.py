import numpy as np
import matplotlib.pyplot as plt

def simulate_rolling_dice(n):
    sum = 0
    dice_1 = []
    dice_2 = []
    dice_3 = []
    sum_arr = []
    for i in range(n):
        rnum = np.random.random_integers(6)
        dice_1.append(rnum)
    for j in range(n):
        rnum = np.random.random_integers(6)
        dice_2.append(rnum)
    for o in range(n):
        rnum = np.random.random_integers(6)
        dice_3.append(rnum)
    for k in range(n):
        sum = dice_1[k] + dice_2[k] + dice_3[k]
        sum_arr.append(sum)  
    
    plt.hist(sum_arr, 16, histtype='stepfilled')        
    plt.show()
    
simulate_rolling_dice(int(input('Enter number of throws: ')))