import random
r = float(input("Введите значение для R: "))
print("I   X   I   Y   I Попадание I")
print("I-------I-------I-----------I")
for n in range(10):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    flag = False
    if (x >= 0) and (x <= r) and (y >= 0) and (y <= r) and (x ** 2 + y ** 2 <= r ** 2) and (y >= x):
        flag = True
    elif (x >= -r) and (x <= 0) and (y >= -r) and (y <= 0) and (x ** 2 + y ** 2 <= r ** 2) and (y <= x):
        flag = True
    print("I{0: 7.2f} I{1: 7.2f} I".format(x, y), end="")
    if flag:
        print("     Да  I")
    else:
        print("     Нет I")
print("I-------I-------I-----------I")