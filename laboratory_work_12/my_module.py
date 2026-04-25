"""
Собственный модуль с константами и функциями
для лабораторной работы №12
"""
from math import sqrt

# Константы
GOLDEN_RATIO = (1 + sqrt(5)) / 2
PI = 3.14159
E = 2.71828

# __all__ определяет, что будет импортировано при "from my_module import *"
__all__ = ['GOLDEN_RATIO', 'PI', 'circle_area', 'circle_perimeter',
           'rectangle_area', 'rectangle_perimeter']


def circle_area(r):
    """Площадь круга по радиусу"""
    from math import pi
    return pi * r ** 2


def circle_perimeter(r):
    """Длина окружности по радиусу"""
    from math import pi
    return 2 * pi * r


def rectangle_area(a, b):
    """Площадь прямоугольника"""
    return a * b


def rectangle_perimeter(a, b):
    """Периметр прямоугольника"""
    return 2 * (a + b)


def _private_function():
    """Приватная функция (не попадёт в импорт *)"""
    return "Эту функцию нельзя импортировать через *"


if __name__ == '__main__':
    print("Модуль my_module запущен напрямую")
    print(f"Золотое сечение: {GOLDEN_RATIO}")
    print(f"PI: {PI}")
    print(f"Площадь круга r=5: {circle_area(5):.2f}")
    print(f"Периметр прямоугольника 3x4: {rectangle_perimeter(3, 4)}")
else:
    print(f"Модуль {__name__} импортирован")