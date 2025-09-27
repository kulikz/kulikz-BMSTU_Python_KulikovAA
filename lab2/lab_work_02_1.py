from math import *
x=float(input('Введите значение x='))
if x<-9:
    y=0
elif 9<=x<6:
    y=-sqrt(9-(x+6)**2)
elif 6<=x<-3:
    y=x+3
elif -3<=x<0:
    y=sqrt(9-x**2)
elif 0<=x<3:
    y=-x+3
elif x>=3:
    y= 0.5*x -1.5
print("X={0:.2f} Y={1:.2f}".format(x, y))