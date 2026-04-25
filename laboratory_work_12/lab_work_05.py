"""
Лабораторная работа №5 (в виде модуля)
Работа с матрицами
"""
from random import uniform

__all__ = ['generate_matrix', 'sum_columns_without_negative',
           'min_diagonal_abs_sum', 'main']


def generate_matrix(size):
    """Генерация квадратной матрицы"""
    matr = []
    for i in range(size):
        matr.append([])
        for j in range(size):
            matr[i].append(round(uniform(-10, 10), 2))
    return matr


def sum_columns_without_negative(matr):
    """Сумма элементов в столбцах без отрицательных элементов"""
    total_sum = 0
    for j in range(len(matr)):
        has_negative = False
        col_sum = 0
        for i in range(len(matr)):
            if matr[i][j] < 0:
                has_negative = True
            col_sum += matr[i][j]
        if not has_negative:
            total_sum += col_sum
            print(f"Столбец {j}: сумма = {col_sum:.2f}")
    return total_sum


def min_diagonal_abs_sum(matr):
    """Минимум среди сумм модулей элементов диагоналей"""
    n = len(matr)
    min_sum = float('inf')

    for k in range(2 * n - 1):
        current_sum = 0
        for i in range(n):
            j = k - i
            if 0 <= j < n:
                current_sum += abs(matr[i][j])
        if 0 < current_sum < min_sum:
            min_sum = current_sum
        print(f"Диагональ i+j={k}: сумма модулей = {current_sum:.2f}")

    return min_sum


def main():
    """Основная функция лабораторной работы №5"""
    n = int(input("Введите размер матрицы: "))
    a = generate_matrix(n)

    print("Матрица:")
    for row in a:
        print(' '.join(f'{elem:7.2f}' for elem in row))

    print("\n1. Сумма элементов в столбцах без отрицательных элементов:")
    sum_result = sum_columns_without_negative(a)
    print(f"Общая сумма: {sum_result:.2f}")

    print("\n2. Минимум среди сумм модулей элементов диагоналей:")
    min_result = min_diagonal_abs_sum(a)
    print(f"Минимальная сумма: {min_result:.2f}")


if __name__ == "__main__":
    print("Модуль lab_work_05 запущен как программа")
    main()