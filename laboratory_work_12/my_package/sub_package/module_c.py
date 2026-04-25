"""
Модуль операций со списками
Использует относительный импорт из родительского пакета
"""
from .. import module_a  # относительный импорт

__all__ = ['avg', 'filter_even', 'min_max', 'flatten']


def avg(lst):
    """Среднее арифметическое элементов списка"""
    return sum(lst) / len(lst) if lst else 0


def filter_even(lst):
    """Фильтрация чётных чисел (использует module_a.is_even)"""
    return [x for x in lst if module_a.is_even(x)]


def min_max(lst):
    """Минимум и максимум списка"""
    return min(lst), max(lst)


def flatten(lst):
    """Выпрямление вложенного списка"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result