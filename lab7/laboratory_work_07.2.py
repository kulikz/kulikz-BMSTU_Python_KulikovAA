import turtle as tr
import random
import math


def fun2_2(x, y):
    if x < -9:
        if y == 0:
            return 1
        else:
            return 0
    elif -9 <= x < -6:
        circle_y = -math.sqrt(9 - (x + 6) ** 2)
        if 0 <= y <= circle_y:
            return 1
        else:
            return 0
    elif -6 <= x < -3:
        line_y = x + 3
        if 0 <= y <= line_y:
            return 1
        else:
            return 0
    elif -3 <= x < 0:
        circle_y = math.sqrt(9 - x ** 2)
        if 0 <= y <= circle_y:
            return 1
        else:
            return 0
    elif 0 <= x < 3:
        line_y = -x + 3
        if 0 <= y <= line_y:
            return 1
        else:
            return 0
    elif x >= 3:
        line_y = 0.5 * x - 1.5
        if 0 <= y <= line_y:
            return 1
        else:
            return 0
    return 0


def calculate_exact_area():
    s1 = 3 * 3
    s2 = (3 * 3) / 2
    s3 = (math.pi * 3 ** 2) / 4
    s4 = (3 * 3) / 2
    s5 = (4 * 2) / 2
    total = s1 + s2 + s3 + s4 + s5
    return total


def main():
    aX = [-12, 8]
    aY = [-4, 4]
    Dx = 800
    Dy = int(Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0])))

    tr.setup(Dx, Dy)
    tr.reset()

    Nmax = 10000

    tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

    tr.title("Lab_7_2_1 Monte-Carlo")
    tr.width(2)
    tr.ht()
    tr.tracer(0, 0)

    tr.color("blue", "blue")

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
        tr.goto(x, 0.1)
        tr.down()
        tr.goto(x, 0)
        tr.up()
        tr.sety(-0.4)
        coords = str(x)
        tr.write(coords)

    for y in range(int(aY[0]), int(aY[1])):
        tr.goto(0, y)
        tr.down()
        tr.goto(0.1, y)
        tr.up()
        tr.setx(0.2)
        coords = str(y)
        tr.write(coords)

    poli = [0, 0.1, 0, -0.1, 0]
    Arrbeg = int(aX[1])
    Xpoli = [Arrbeg, Arrbeg - 0.1, Arrbeg + 0.3, Arrbeg - 0.1, Arrbeg]

    tr.goto(Xpoli[0], poli[0])
    tr.begin_fill()
    tr.down()

    for i in range(1, 5):
        tr.goto(Xpoli[i], poli[i])
    tr.end_fill()

    tr.up()
    tr.goto(Arrbeg, -0.7)
    tr.write("X", font=("Arial", 14, "bold"))

    Arrbeg = int(aY[1])
    Ypoli = [Arrbeg, Arrbeg - 0.1, Arrbeg + 0.3, Arrbeg - 0.1, Arrbeg]

    tr.up()
    tr.goto(poli[0], Ypoli[0])
    tr.begin_fill()
    tr.down()

    for i in range(1, 5):
        tr.goto(poli[i], Ypoli[i])
    tr.end_fill()

    tr.up()
    tr.goto(0.2, Arrbeg)
    tr.write("Y", font=("Arial", 14, "bold"))

    tr.up()
    mfun = 0

    for n in range(Nmax):
        x = random.uniform(aX[0], aX[1])
        y = random.uniform(aY[0], aY[1])
        tr.goto(x, y)

        if fun2_2(x, y) != 0:
            tr.dot(3, "green")
            mfun += 1
        else:
            tr.dot(1, "#ffccff")

    Srect = (aX[1] - aX[0]) * (aY[1] - aY[0])
    Sf = Srect * mfun / Nmax

    exact_area = calculate_exact_area()
    error_percent = abs((Sf - exact_area) / exact_area) * 100

    tr.goto(-10, 3.5)
    meseg = f"N = {Nmax}\nNF = {mfun}\nS (MC) = {Sf:.4f}\nS (exact) = {exact_area:.4f}\nError = {error_percent:.2f}%"
    tr.write(meseg, font=("Arial", 12, "bold"))

    print(f"N = {Nmax}")
    print(f"NF = {mfun}")
    print(f"S (Monte-Carlo) = {Sf:.4f}")
    print(f"S (exact) = {exact_area:.4f}")
    print(f"Error = {error_percent:.2f}%")

    tr.done()


if __name__ == "__main__":
    main()