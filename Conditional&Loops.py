# -*- coding: utf-8 -*-
"""
Created on Wed May 25 12:10:51 2022

@author: LAPTOP-VQE49TEL
"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    #dollars = dollars_to_float(input("What is the cost of your meal?"))
    #percents = percent_to_float(input("How much percents?"))
   #tip = dollars * percents
   # print("You should leave {0:0.2f} dollars".format(tip))
  #  fact = 1
    #n = int(input("Input an integer > 1\n"))
   # x = np.array([[1,2,3],[4,5,6],[7,8,9]])
    #invest = float(input("How much money you want to deposit on your bank account?\n"))
   # prime_numbers(n)
   # fact_for(fact)
   # fact_while(fact)
   # prime_numbers(n)
   # matrix(x)
    #annual(invest)
   #monthly(invest)
    #daily(invest)
    day_of_week()
def dollars_to_float(d):
    d = float(d.strip('$'))
    return d


def percent_to_float(p):
    p = float(p.strip('%'))
    p = p / 100
    return p
        

#issue 1


    

def fact_for(x):
    for i in range(1, 11, 1):
        x = x * i    
    print(x)
def fact_while(y):
    y, i_while =1,1
    while i_while <=10:
        y = y * i_while
        i_while += 1
   
    print(y)  



#issue 2
   
    
def prime_numbers(x):
    i = 2
    while x%i !=0:
        i +=1
    if x/i == 1: print("n is a prime number") 
    print("the smallest factor of {0:d} is {1:d}".format(x,i))



#issue 3
def matrix(x):
    for a in x:  
        print(a[2], end=' ')
    print()
    for a in x:
        print(a[1]*a[1]*2, end=' ')



#issue 4
   
    
def annual(a):
    for i in range(1, 11, 1):
        bonus = a * 0.06
        a = a + bonus
    print(a)
def monthly(b):
    for i in range(1, 121, 1):
        bonus = b * (0.06/12)
        b = b + bonus
    print(b)    
def daily(c):
    for i in range(1, 3651, 1):
        bonus = c * (0.06/365)
        c = c + bonus
    print(c) 
    
#issue 5
def dayofweek(d, m, y):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    return (( y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)
 
# Driver Code
def day_of_week():
    day = dayofweek(16, 5, 2111)
    if day == 1:print("Monday")
    elif day == 2:print("Tuesday")
    elif day == 3:print("Wednesday")
    elif day == 4:print("Thursday")
    elif day == 5:print("Friday")
    elif day == 6:print("Saturday")
    elif day == 0:print("Sunday")

main()