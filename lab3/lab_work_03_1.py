from math import *
flag = False
xb = float(input('Введите Xbeg='))
xe = float(input('Введите Xend='))
dx = float(input('Введите Dx='))
print("Xbeg={0: 7.2f} Xend={1: 7.2f}"
 .format(xb, xe))
print(" Dx={0: 7.2f}".format(dx))
xt = xb
print("+--------+--------+")
print("I X I Y I")
print("+--------+--------+")
while xt<= xe:
    if xt<-9:
        y=0
    elif 9<=xt<6:
        y=-sqrt(9-(xt+6)**2)
    elif 6<=xt<-3:
        y=xt+3
    elif -3<=xt<0:
        y=sqrt(9-xt**2)
    elif 0<=xt<3:
        y=-xt+3
    elif xt>=3:
        y=0.5*xt-1.5
    print("I{0: 7.2f} I{1: 7.2f} I"
 .format(xt, y))
    xt += dx
print("+--------+--------+")