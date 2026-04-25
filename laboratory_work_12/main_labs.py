"""
Демонстрация импорта функций из лабораторных работ 1, 4, 5
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("ДЕМОНСТРАЦИЯ ИМПОРТА ЛАБОРАТОРНЫХ РАБОТ")
print("=" * 60)

# 1. Импорт всего модуля из лабы 1
print("\n--- Лабораторная работа №1 (импорт модуля) ---")
import lab_work_01

angle = 1.2
print(f"Угол: {angle} рад")
print(f"Выражение 1: {lab_work_01.calculate_expression1(angle):.4f}")
print(f"Выражение 2: {lab_work_01.calculate_expression2(angle):.4f}")

# 2. Импорт конкретных функций из лабы 4
print("\n--- Лабораторная работа №4 (импорт функций) ---")
from lab_work_04 import generate_array, find_last_positive_index, sum_before_index

arr = generate_array(8)
print(f"Массив: {arr}")
last_pos = find_last_positive_index(arr)
print(f"Индекс последнего положительного: {last_pos}")
print(f"Сумма до него: {sum_before_index(arr, last_pos):.3f}")

# 3. Импорт с переименованием из лабы 5
print("\n--- Лабораторная работа №5 (импорт с переименованием) ---")
from lab_work_05 import generate_matrix as gen_mat
from lab_work_05 import sum_columns_without_negative as sum_cols
from lab_work_05 import min_diagonal_abs_sum as min_diag

matrix = gen_mat(4)
print("Матрица 4x4:")
for row in matrix:
    print(' '.join(f'{elem:7.2f}' for elem in row))
print(f"Сумма столбцов без отрицательных: {sum_cols(matrix):.2f}")
print(f"Мин. сумма диагоналей: {min_diag(matrix):.2f}")