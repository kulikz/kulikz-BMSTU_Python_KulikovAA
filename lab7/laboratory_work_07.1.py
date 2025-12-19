import turtle as tr
import math


def my_fun(x):
    if x < -9:
        y = 0
    elif -9 <= x < -6:
        y = -math.sqrt(9 - (x + 6) ** 2)
    elif -6 <= x < -3:
        y = x + 3
    elif -3 <= x < 0:
        y = math.sqrt(9 - x ** 2)
    elif 0 <= x < 3:
        y = -x + 3
    elif x >= 3:
        y = 0.5 * x - 1.5
    return y


def main():
    xb = -12
    xe = 8
    dx = 0.1

    aX = [xb - 2, xe + 2]
    y_min = -4
    y_max = 4
    aY = [y_min, y_max]

    Dx = 800
    Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
    tr.setup(Dx, Dy)
    tr.reset()

    tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

    tr.title("Лабораторная работа 7.1: График функции")
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
            tr.sety(-0.4)
            tr.write(str(x))

    for y in range(int(aY[0]), int(aY[1])):
        if y % 2 == 0 and y != 0:
            tr.goto(0, y)
            tr.down()
            tr.goto(0.1, y)
            tr.up()
            tr.setx(0.3)
            tr.write(str(y))

    tr.color("blue")
    tr.width(3)

    x = xb
    y = my_fun(x)
    tr.up()
    tr.goto(x, y)
    tr.down()

    while x <= xe:
        y = my_fun(x)
        tr.goto(x, y)
        x += dx

    tr.up()
    tr.goto(-10, 3.5)
    tr.color("red")
    tr.write("График функции", font=("Arial", 14, "bold"))

    tr.goto(-10, 3.0)
    tr.write("Вариант 1", font=("Arial", 10))

    tr.mainloop()


if __name__ == "__main__":
    main()