"""
Демонстрация различных способов импорта модуля my_module
"""

print("=" * 60)
print("ДЕМОНСТРАЦИЯ ИМПОРТА МОДУЛЯ my_module")
print("=" * 60)

# 1. Импорт всего модуля
print("\n--- 1. Импорт всего модуля ---")
import my_module

print(f"Золотое сечение: {my_module.GOLDEN_RATIO}")
print(f"Площадь круга r=5: {my_module.circle_area(5):.2f}")
print(f"Площадь прямоугольника 3x4: {my_module.rectangle_area(3, 4)}")

# 2. Импорт конкретных элементов
print("\n--- 2. Импорт конкретных элементов ---")
from my_module import circle_perimeter, rectangle_perimeter

print(f"Периметр круга r=5: {circle_perimeter(5):.2f}")
print(f"Периметр прямоугольника 3x4: {rectangle_perimeter(3, 4)}")

# 3. Импорт с переименованием
print("\n--- 3. Импорт с переименованием ---")
import my_module as mm
from my_module import rectangle_area as rect_a

print(f"Площадь круга r=3 (mm): {mm.circle_area(3):.2f}")
print(f"Площадь прямоугольника 2x5 (rect_a): {rect_a(2, 5)}")

# 4. Импорт всех элементов (только то, что в __all__)
print("\n--- 4. Импорт всех элементов (from module import *) ---")
from my_module import *

print(f"Золотое сечение: {GOLDEN_RATIO}")
print(f"PI: {PI}")
print(f"Площадь круга r=7: {circle_area(7):.2f}")
print(f"Периметр прямоугольника 2x3: {rectangle_perimeter(2, 3)}")