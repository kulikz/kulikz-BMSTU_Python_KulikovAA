"""
Модуль строковых операций
"""

__all__ = ['reverse_str', 'count_vowels', 'is_palindrome', 'repeat']


def reverse_str(s):
    """Реверс строки"""
    return s[::-1]


def count_vowels(s):
    """Подсчёт гласных букв в строке"""
    return sum(1 for c in s.lower() if c in 'aeiouаеёиоуыэюя')


def is_palindrome(s):
    """Проверка строки на палиндром"""
    s = s.lower().replace(' ', '')
    return s == s[::-1]


def repeat(s, n):
    """Повтор строки n раз"""
    return s * n