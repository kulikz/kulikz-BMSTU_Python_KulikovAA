"""
Демонстрация различных способов импорта из пакета my_package
"""

print("=" * 60)
print("ДЕМОНСТРАЦИЯ ИМПОРТА ИЗ ПАКЕТА")
print("=" * 60)

# 1. Импорт модуля из пакета
print("\n--- 1. Импорт модуля из пакета ---")
import my_package.module_a

print(f"4! = {my_package.module_a.factorial(4)}")
print(f"Сумма цифр 1234: {my_package.module_a.digit_sum(1234)}")
print(f"clamp(15, 0, 10): {my_package.module_a.clamp(15, 0, 10)}")

# 2. Импорт определённых элементов из модуля в пакете
print("\n--- 2. Импорт конкретных элементов из модуля в пакете ---")
from my_package.module_b import is_palindrome, reverse_str

print(f"'radar' палиндром? {is_palindrome('radar')}")
print(f"Реверс 'hello': {reverse_str('hello')}")
print(f"'А роза упала на лапу Азора' палиндром? {is_palindrome('А роза упала на лапу Азора')}")

# 3. Импорт из подпакета
print("\n--- 3. Импорт из подпакета ---")
from my_package.sub_package import module_c

print(f"Среднее [1,2,3,4,5]: {module_c.avg([1, 2, 3, 4, 5])}")
print(f"Чётные из [1,2,3,4,5,6]: {module_c.filter_even([1, 2, 3, 4, 5, 6])}")
print(f"min_max [5,2,8,1]: {module_c.min_max([5, 2, 8, 1])}")

# 4. Импорт конкретного элемента из подпакета
print("\n--- 4. Импорт конкретного элемента из подпакета ---")
from my_package.sub_package.module_c import flatten

print(f"Flatten [[1,2],[3,[4,5]]]: {flatten([[1, 2], [3, [4, 5]]])}")