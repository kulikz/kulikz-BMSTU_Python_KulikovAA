from math import *
from random import *

r=float(input("Введите значение для R: "))
flag=False
print("I   X   I   Y   I Попадание I")
for n in range (10):
    x= uniform(-r,r)
    y= uniform(-r,r)
    if (x >= 0) and (x <= r) and (y >= 0) and (y <= r) and (x ** 2 + y ** 2 <= r ** 2) and (y >= x):
        flag = True
    elif (x >= -r) and (x <= 0) and (y >= -r) and (y <= 0) and (x ** 2 + y ** 2 <= r ** 2) and (y <= x):
        flag = True
    print("{0: 7.2f} {1: 7.2f}".format(x, y), end="      ")
    if flag:
        print("Да")
    else:
        print("Нет")
    print("I-------I-------I-----------I")
