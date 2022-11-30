# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy
import string
import re


    
'''
# issue №1

g, h0, v0, t =9.8, 1.6, 14.2, 2
print("Initial height is = " + str(h0) + " m")
print("Initial velocity is = " + str(v0) + " m/s")
h = h0 + v0*t - (0.5*(g*(t*t)))
v = v0 - g*t
print("Height is = " + str(h) + " m")
print("Velocity is = " + str(v) + " m/s") 
"""


V0, a, z = 10, 2.5, 13
V = V0*(1 - (z/numpy.sqrt(a**2+z**2)))
print(V)


#issue №3a, b, c

a = (2+numpy.exp(2.8))/(numpy.sqrt(13)-2)
print(a)

b = (1 - ((1+numpy.log2(2))**-3.5))/(1+numpy.sqrt(5))
print(b)
c = numpy.sin((2-numpy.sqrt(2))/(2+numpy.sqrt(2)))
print(c)


#issue №4

a, b, c = 1.0, 0, 4
a = a+0j
x1 = (-b + numpy.sqrt((b*b)-(4*a*c)))/(2*a)
x2 = (-b - numpy.sqrt((b*b)-(4*a*c)))/(2*a)
print("x1 is = " + str(x1))
print("x2 is = " + str(x2))

#issue №5
d, n1, n2, n3, n4, n5, n6 =1, 3, 4, 5, 100, 10000, 100000
p1 = n1 * d * numpy.sin(numpy.pi/n1)
p2 = n2 * d * numpy.sin(numpy.pi/n2)
p3 = n3 * d * numpy.sin(numpy.pi/n3)
p4 = n4 * d * numpy.sin(numpy.pi/n4)
p5 = n5 * d * numpy.sin(numpy.pi/n5)
p6 = n6 * d * numpy.sin(numpy.pi/n6)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)



 
def n_nn_nnn():
    n = int(input("Enter the number: "))
    sum_of_n = n + (n*10+n) +(n*100+n*10+n)
    print(sum_of_n)
   
def sum_two_smallest_nums():
    numlst = [3, 6, 5, 98, 55, 2, 11, 36]
    length = len(numlst)
    for i in range(length):
        for j in range(length - 1):
            if numlst[j] > numlst[j+1]:
                temp = numlst[j]
                numlst[j] = numlst[j+1]
                numlst[j+1] = temp
            j+=1
        i+=1
    print(numlst)
    print(numlst[0] + numlst[1])
'''

def main():
    #sum_of_numbers()
    #n_nn_nnn()
    #sum_two_smallest_nums()
    #coke_machine()
    '''
    while True:
        str = input()
        if isvalid(str):
            print("Valid")
        else: 
            print("Invalid")
    '''
    #while True:
        #str = input().upper()
        #print(str)
        #isvalid(str)
    #camelcase(str)
    #nutrition()
    #taqueria()
    #club_pass('addiction')
    #?grocery_list()
    #outdated()
    count_grocery()
    


    
def isvalid(str):
    plate = str
    if isalpha_plate(plate) and isnum_plate(plate) and islen_plate(plate) and ispunct_plate(plate):
        return True
    else:
        return False
    
def isalpha_plate(str):
    plate = str
    if plate[0:2].isalpha():
        return True
    else: 
        return False
    
def isnum_plate(str):
    plate = str
    if plate[-2:].isdigit() and plate[-2]!='0':
        return True
    else: 
        return False
def islen_plate(str):
    plate = str
    if 2<=len(plate)<=6:
        return True
    else: 
        return False
def ispunct_plate(str):
    plate = str
    if plate[:].isalnum():
       return True
    else: 
       return False
def camelcase(str):
    phrase = str
    for i in phrase:
        if i.isupper():
            print('_'+i.lower(), end='')
        else:
            print(i, end='')
    
    
def coke_machine():
        amount_due = 50
        while True:
            print("Need to put: " + str(amount_due))
            coin = int(input("Put coins into the machine: "))
            print("You've put: " + str(coin))
            if coin == 25 or coin == 10 or coin == 5:
                amount_due -=coin
            else:
                print("coin is not accepted")
            if amount_due <= 0:
                print("Change owed: " + str(-amount_due))
                return
def vowel_deleter(str):
    word = str
    vowels = ['a','o','e','i','u']
    for i in word:
        if i in vowels:
            i = ''
            print(i, end='')
        else:
            print(i, end='')
def nutrition():
    dict = {'apple':130, 'banana':110, 'pear':90, 'peach': 150, 'orange': 50}
    while True:
        input_fruites = input('Item: ')
        if input_fruites in dict:
            print("Calories: " + str(dict[input_fruites]))
        else:
            print('', end='')
        if input_fruites == 'q':
            break
def taqueria():
    dict_menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    total = 0
    while True:
        inp = input("Please, enter dish from the menu: ").title()
        if inp in dict_menu:
            total +=dict_menu[inp] 
            print("Total: $"+str(total))
        elif inp == 'Q':
            return
        else:
            pass
    
        
def grocery_list():
    dict_grocery = {'apple':1, 'banana':1, 'pear':1, 'peach': 1, 'orange':1}
    grocery_cont = []
    while True:
        str1 = input()
        grocery_cont.append(str1)
        if str1 == 'q':
            break
    grocery_cont.sort()
    for i in range(len(grocery_cont)-1):
        print(grocery_cont[i].upper())
def outdated():
    dict_data={"January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
        }
    data = input().replace(',', '')
    data = re.split(' ', data)
    m, d, y= data
    if m in dict_data:
        print(y, f"{dict_data[m]:02}", d, sep='-')
    #print(y, m, d, sep='-')

def count_grocery():
        dict_grocery = {'apple':1, 'banana':1, 'pear':1, 'peach': 1, 'orange':1}
        grocery_cont = []
        while True:
            str1 = input()
            grocery_cont.append(str1)
            if str1 == 'q':
                break
    
        
               
main()