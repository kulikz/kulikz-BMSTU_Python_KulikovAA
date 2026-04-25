"""
Демонстрация различных способов импорта модуля laboratory_work_12_module
"""

print("=" * 60)
print("ДЕМОНСТРАЦИЯ ИМПОРТА МОДУЛЯ")
print("=" * 60)

# 1. Импорт всего модуля
print("\n--- 1. Импорт всего модуля ---")
import laboratory_work_12_module as lw12

print(f"PI = {lw12.PI}")
print(f"add(5, 10) = {lw12.add(5, 10)}")
print(f"multiply(3, 7) = {lw12.multiply(3, 7)}")

# 2. Импорт конкретных элементов
print("\n--- 2. Импорт конкретных элементов ---")
from laboratory_work_12_module import add, substract, PI

print(f"PI = {PI}")
print(f"add(10, 20) = {add(10, 20)}")
print(f"substract(20, 7) = {substract(20, 7)}")

# 3. Импорт с переименованием
print("\n--- 3. Импорт с переименованием ---")
from laboratory_work_12_module import multiply as mul, divide as div

print(f"multiply(6, 8) = {mul(6, 8)}")
print(f"divide(100, 4) = {div(100, 4)}")

# 4. Импорт всех элементов (только те, что в __all__)
print("\n--- 4. Импорт всех элементов (from module import *) ---")
from laboratory_work_12_module import *

print(f"PI = {PI}")
print(f"add(1, 2) = {add(1, 2)}")
print(f"multiply(3, 4) = {multiply(3, 4)}")
print(f"divide(10, 2) = {divide(10, 2)}")