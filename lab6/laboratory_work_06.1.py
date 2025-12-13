# -*- coding: cp1251 -*-
from math import *


def f1(a, x):
    result = (2 * sin(3 * pi - 2 * a) ** 2) * cos(5 * pi + 2 * a) ** 2
    return result


def f2(x):
    result = 1 / 4 - 1 / 4 * sin(5 / 2 * pi - 8 * x)
    return result


def create_input_file():
    """Создание входного файла с тестовыми данными"""
    with open("lab1_input.txt", "w", encoding="utf-8") as fi:
        fi.write("# Лабораторная работа №1\n")
        fi.write("# a (угол в радианах)\n")
        fi.write("#---\n")
        test_data = [0.1, 0.5, 1.0, 1.57, 2.0, 2.5, 3.0, 3.14]
        for value in test_data:
            fi.write(f"{value}\n")
    print("Создан файл lab1_input.txt")


def main():
    create_input_file()

    fi = open("lab1_input.txt", "rt", encoding="utf-8")
    fo = open("lab1_output.txt", "wt", encoding="utf-8")

    # Пропускаем строки заголовка
    line = fi.readline()
    line = fi.readline()
    line = fi.readline()

    fo.write("+----------+----------+------------+\n")
    fo.write("|    a     |   f1(a)  |    f2(a)   |\n")
    fo.write("+----------+----------+------------+\n")

    for line in fi:
        line = line.strip()
        if not line:
            continue
        a = float(line)
        fo.write("| {0:8.4f} | {1:8.4f} | {2:10.4f} |\n".format(a, f1(a, a), f2(a)))

    fo.write("+----------+----------+------------+\n")

    fi.close()
    fo.close()
    print("Результаты записаны в lab1_output.txt")


if __name__ == "__main__":
    main()