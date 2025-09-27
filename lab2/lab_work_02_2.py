from math import *
flag = 0
print('Введите параметр R:')
R = float(input('R = '))
print('Введите координаты X и Y для точки:')
x = float(input('X = '))
y = float(input('Y = '))
if (x >= 0) and (x <= R) and (y >= 0) and (y <= R) and (x**2 + y**2 <= R**2) and (y >= x):
    flag = 1
elif (x >= -R) and (x <= 0) and (y >= -R) and (y <= 0) and (x**2 + y**2 <= R**2) and (y <= x):
    flag = 1
print("Точка X ={0:6.2f} Y ={1:6.2f}".format(x, y), end=" ")
if flag:
    print("попадает")
else:
    print("не попадает")