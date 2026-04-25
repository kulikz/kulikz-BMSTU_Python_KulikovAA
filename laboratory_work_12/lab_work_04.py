"""
Лабораторная работа №4 (в виде модуля)
Работа с массивами
"""
import random

__all__ = ['generate_array', 'find_last_positive_index',
           'sum_before_index', 'filter_by_abs_range', 'main']


def generate_array(n, min_val=-5.0, max_val=5.0):
    """Генерация массива случайных чисел"""
    return [round(random.uniform(min_val, max_val), 3) for _ in range(n)]


def find_last_positive_index(array):
    """Поиск индекса последнего положительного элемента"""
    for i in range(len(array) - 1, -1, -1):
        if array[i] > 0:
            return i
    return -1


def sum_before_index(array, index):
    """Сумма элементов до указанного индекса"""
    return sum(array[:index]) if index != -1 else 0


def filter_by_abs_range(array, a, b):
    """Фильтрация массива: удаление элементов с |x| в [a,b] и замена на 0"""
    result = array.copy()
    i = 0
    removed_count = 0
    while i < len(result):
        if a <= abs(result[i]) <= b:
            result.pop(i)
            removed_count += 1
        else:
            i += 1
    result.extend([0.0] * removed_count)
    return result


def main():
    """Основная функция лабораторной работы №4"""
    n = int(input("Введите длину массива: "))
    array = generate_array(n)

    print("Массив до преобразования:")
    print(array)

    max_element = max(array)
    print(f"Максимальный элемент: {max_element}")

    last_idx = find_last_positive_index(array)
    sum_before = sum_before_index(array, last_idx)
    print(f"Сумма до последнего положительного: {sum_before}")

    a = float(input("Введите значение границы a: "))
    b = float(input("Введите значение границы b: "))

    filtered = filter_by_abs_range(array, a, b)
    print("Массив после преобразования:")
    print(filtered)


if __name__ == "__main__":
    print("Модуль lab_work_04 запущен как программа")
    main()