import turtle as tr
import math


def series_sum(x, eps):
    an = x
    n = 1
    y = an
    while abs(an) >= eps:
        k = -(x ** 2) / ((2 * n + 1) * (2 * n + 2) * (2 * n + 3))
        an = an * k
        y = y + an
        n = n + 1
    return y, n


def main():
    x_beg = -3
    x_end = 3
    dx = 0.1
    eps = 0.001

    aX = [x_beg - 0.5, x_end + 0.5]
    aY = [-2, 2]

    Dx = 800
    Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
    tr.setup(Dx, Dy)
    tr.reset()

    tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

    tr.title("Лабораторная работа 7.3: Разложение в ряд")
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
        if x % 1 == 0:
            tr.goto(x, 0.05)
            tr.down()
            tr.goto(x, 0)
            tr.up()
            tr.sety(-0.3)
            tr.write(str(x))

    for y in range(int(aY[0]), int(aY[1])):
        if y % 1 == 0 and y != 0:
            tr.goto(0, y)
            tr.down()
            tr.goto(0.05, y)
            tr.up()
            tr.setx(0.2)
            tr.write(str(y))

    tr.color("red")
    tr.width(2)

    x = x_beg
    y, n = series_sum(x, eps)
    tr.up()
    tr.goto(x, y)
    tr.down()

    while x <= x_end:
        y, n = series_sum(x, eps)
        tr.goto(x, y)
        x += dx

    tr.up()
    tr.goto(-2.5, 1.5)
    tr.color("blue")
    tr.write("Разложение sin(x) в ряд", font=("Arial", 12, "bold"))

    tr.goto(-2.5, 1.3)
    tr.write(f"Точность: ε = {eps}", font=("Arial", 10))

    tr.goto(-2.5, -1.8)
    tr.write(f"Диапазон: x ∈ [{x_beg}, {x_end}]", font=("Arial", 9))

    tr.mainloop()


if __name__ == "__main__":
    main()