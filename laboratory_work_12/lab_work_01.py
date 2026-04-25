"""
Лабораторная работа №1 (в виде модуля)
Вычисление тригонометрических выражений
"""
from math import cos, sin

__all__ = ['calculate_expression1', 'calculate_expression2', 'main']


def calculate_expression1(angle):
    """Вычисление первого выражения"""
    return 1 - 0.25 * sin(2 * angle) ** 2 + cos(2 * angle)


def calculate_expression2(angle):
    """Вычисление второго выражения"""
    return cos(angle) ** 2 + cos(angle) ** 4


def main():
    """Основная функция лабораторной работы №1"""
    angle = float(input("Введите значение угла в радианах: "))
    print("Результаты функций:")
    print(f"Первое выражение: {calculate_expression1(angle):.4f}")
    print(f"Второе выражение: {calculate_expression2(angle):.4f}")


if __name__ == '__main__':
    print("Модуль lab_work_01 запущен как программа")
    main()