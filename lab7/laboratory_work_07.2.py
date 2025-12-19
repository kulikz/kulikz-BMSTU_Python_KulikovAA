import turtle as tr
import random
import math


def check_point(x, y, r):
    flag = False
    if (x >= 0) and (x <= r) and (y >= 0) and (y <= r):
        if (x ** 2 + y ** 2 <= r ** 2) and (y >= x):
            flag = True
    elif (x >= -r) and (x <= 0) and (y >= -r) and (y <= 0):
        if (x ** 2 + y ** 2 <= r ** 2) and (y <= x):
            flag = True
    return flag


def main():
    r = 5

    aX = [-r - 1, r + 1]
    aY = [-r - 1, r + 1]

    Dx = 600
    Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
    tr.setup(Dx, Dy)
    tr.reset()

    Nmax = 10000

    tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

    tr.title("Лабораторная работа 7.2: Метод Монте-Карло")
    tr.width(2)

    tr.ht()
    tr.tracer(0, 0)

    tr.color("black")

    tr.up()
    tr.goto(aX[0], 0)
    tr.down()
    tr.goto(aX[1], 0)

    tr.up()
    tr.goto(0, aY[1])
    tr.down()
    tr.goto(0, aY[0])

    tr.up()
    for x in range(int(aX[0]), int(aX[1])):
        if x % 2 == 0:
            tr.goto(x, 0.1)
            tr.down()
            tr.goto(x, 0)
            tr.up()
            tr.sety(-0.5)
            tr.write(str(x))

    for y in range(int(aY[0]), int(aY[1])):
        if y % 2 == 0 and y != 0:
            tr.goto(0, y)
            tr.down()
            tr.goto(0.1, y)
            tr.up()
            tr.setx(0.3)
            tr.write(str(y))

    tr.up()
    mfun = 0

    for n in range(Nmax):
        x = random.uniform(aX[0], aX[1])
        y = random.uniform(aY[0], aY[1])
        tr.goto(x, y)

        if check_point(x, y, r):
            tr.dot(2, "green")
            mfun += 1
        else:
            tr.dot(1, "#ffccff")

    Srect = (aX[1] - aX[0]) * (aY[1] - aY[0])
    Sf = Srect * mfun / Nmax

    exact_area = (math.pi * r ** 2) / 4
    error_percent = abs((Sf - exact_area) / exact_area) * 100

    tr.up()
    tr.goto(-r + 1, r - 1)
    tr.color("blue")
    meseg = f"Всего точек: {Nmax}\nВнутри фигуры: {mfun}\n"
    meseg += f"Площадь (М-К): {Sf:.4f}\n"
    meseg += f"Точная площадь: {exact_area:.4f}\n"
    meseg += f"Погрешность: {error_percent:.2f}%"
    tr.write(meseg, font=("Arial", 10, "bold"))

    print(f"N = {Nmax}")
    print(f"NF = {mfun}")
    print(f"S (Монте-Карло) = {Sf:.4f}")
    print(f"S (точная) = {exact_area:.4f}")
    print(f"Погрешность = {error_percent:.2f}%")

    tr.mainloop()


if __name__ == "__main__":
    main()