"""
Модуль с математическими операциями
"""

# Константа
PI = 3.14159

# __all__ определяет публичные имена
__all__ = ['PI', 'add', 'substract', 'multiply', 'divide']


def add(a, b):
    """Сложение двух чисел"""
    return a + b


def substract(a, b):
    """Вычитание двух чисел"""
    return a - b


def multiply(a, b):
    """Умножение двух чисел"""
    return a * b


def divide(a, b):
    """Деление двух чисел с проверкой на ноль"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


if __name__ == "__main__":
    print("Модуль запущен как программа")
    print(f"add(2, 30) = {add(2, 30)}")
    print(f"PI = {PI}")
else:
    print("Модуль импортирован")