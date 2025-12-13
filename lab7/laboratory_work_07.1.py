# -*- coding: utf-8 -*-
import turtle as tr
import math

def function_variant1(x):
    if x < -9:
        return 0
    elif -9 <= x < -6:
        # Нижняя полуокружность с центром (-6, 0), радиус 3
        return -math.sqrt(9 - (x + 6) ** 2)
    elif -6 <= x < -3:
        # Прямая линия
        return x + 3
    elif -3 <= x < 0:
        # Верхняя полуокружность с центром (0, 0), радиус 3
        return math.sqrt(9 - x ** 2)
    elif 0 <= x < 3:
        # Прямая линия
        return -x + 3
    else:  # x >= 3
        # Прямая линия
        return 0.5 * x - 1.5
def setup_window():
    x_min, x_max = -12, 10
    y_min, y_max = -4, 4

    screen_width = 900
    screen_height = 600

    screen = tr.Screen()
    screen.setup(screen_width, screen_height)
    screen.setworldcoordinates(x_min, y_min, x_max, y_max)
    screen.title("Лабораторная работа №7, Задание 1. График функции (Вариант 1)")
    screen.bgcolor("white")

    return screen, x_min, x_max, y_min, y_max


def draw_coordinate_system(x_min, x_max, y_min, y_max):
    tr.color("black")
    tr.width(1)

    tr.up()
    tr.goto(x_min, 0)
    tr.down()
    tr.goto(x_max, 0)

    tr.up()
    tr.goto(x_max - 0.5, 0.3)
    tr.down()
    tr.goto(x_max, 0)
    tr.goto(x_max - 0.5, -0.3)

    tr.up()
    tr.goto(0, y_min)
    tr.down()
    tr.goto(0, y_max)

    tr.up()
    tr.goto(0.3, y_max - 0.5)
    tr.down()
    tr.goto(0, y_max)
    tr.goto(-0.3, y_max - 0.5)

    tr.up()
    tr.goto(x_max - 0.8, -0.8)
    tr.write("X", font=("Arial", 12, "bold"))

    tr.goto(0.8, y_max - 0.8)
    tr.write("Y", font=("Arial", 12, "bold"))


def draw_grid_and_ticks(x_min, x_max, y_min, y_max):
    tr.color("lightgray")
    tr.width(0.5)

    for x in range(int(x_min), int(x_max) + 1):
        if x != 0:  # Пропускаем ось Y
            tr.up()
            tr.goto(x, y_min)
            tr.down()
            tr.goto(x, y_max)

    for y in range(int(y_min), int(y_max) + 1):
        if y != 0:  # Пропускаем ось X
            tr.up()
            tr.goto(x_min, y)
            tr.down()
            tr.goto(x_max, y)

    tr.color("black")
    for x in range(int(x_min), int(x_max) + 1):
        if x % 2 == 0:  # Только четные значения для читаемости
            tr.up()
            tr.goto(x, -0.2)
            tr.down()
            tr.goto(x, 0.2)
            tr.up()
            tr.goto(x - 0.1, -0.5)
            tr.write(str(x), align="center", font=("Arial", 8, "normal"))

    for y in range(int(y_min), int(y_max) + 1):
        if y % 2 == 0 and y != 0:  # Только четные, кроме 0
            tr.up()
            tr.goto(-0.2, y)
            tr.down()
            tr.goto(0.2, y)
            tr.up()
            tr.goto(0.5, y - 0.2)
            tr.write(str(y), align="left", font=("Arial", 8, "normal"))


def draw_function_graph(x_min, x_max, num_points=2000):
    tr.color("blue")
    tr.width(2)

    dx = (x_max - x_min) / num_points

    tr.up()

    drawing = False

    for i in range(num_points + 1):
        x = x_min + i * dx
        y = function_variant1(x)

        tr.goto(x, y)

        if i == 0 or not drawing:
            tr.down()
            drawing = True

    tr.up()
    tr.color("red")
    tr.goto(-11, 3.2)
    tr.write("График функции (Вариант 1)", font=("Arial", 14, "bold"))

    tr.goto(-11, 2.7)
    tr.write("f(x) = ", font=("Arial", 10, "bold"))

    equations = [
        "0,                          x < -9",
        "-√(9 - (x + 6)²),        -9 ≤ x < -6",
        "x + 3,                   -6 ≤ x < -3",
        "√(9 - x²),              -3 ≤ x < 0",
        "-x + 3,                   0 ≤ x < 3",
        "0.5x - 1.5,                x ≥ 3"
    ]

    for j, eq in enumerate(equations):
        tr.goto(-10, 2.2 - j * 0.3)
        tr.write(eq, font=("Courier", 9, "normal"))

def draw_function_parts():
    colors = ["red", "green", "blue", "orange", "purple", "brown"]
    descriptions = [
    tr.up()
    tr.color("black")
    tr.goto(4, 3)
    tr.write("Составные части:", font=("Arial", 10, "bold"))

    for i in range(6):
        tr.goto(4, 2.7 - i * 0.25)
        tr.color(colors[i])
        tr.write("■", font=("Arial", 12, "normal"))
        tr.color("black")
        tr.goto(4.3, 2.7 - i * 0.25)
        tr.write(descriptions[i], font=("Arial", 8, "normal"))

def main():
    screen, x_min, x_max, y_min, y_max = setup_window()
    tr.tracer(0, 0)
    tr.hideturtle()
    draw_coordinate_system(x_min, x_max, y_min, y_max)
    draw_grid_and_ticks(x_min, x_max, y_min, y_max)
    draw_function_graph(x_min, x_max)
    draw_function_parts()
    tr.update()
    tr.up()
    tr.color("darkgray")
    tr.goto(x_min + 0.5, y_min + 0.3)
    tr.write("Лабораторная работа №7, Задание 1. Вариант 1",
             font=("Arial", 8, "italic"))
    print("График построен!")
    print("Для выхода нажмите на окно с графиком.")
    screen.exitonclick()
if __name__ == "__main__":
    main()