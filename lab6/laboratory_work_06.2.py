# -*- coding: utf-8 -*-
import random


def create_input_file():
    """Создание входного файла с тестовыми данными"""
    with open("lab4_input.txt", "w", encoding="utf-8") as fi:
        fi.write("# Лабораторная работа №4\n")
        fi.write("# N (размер массива, 5 <= N <= 30)\n")
        fi.write("#---\n")
        fi.write("12\n")
    print("Создан файл lab4_input.txt")


def main():
    create_input_file()

    with open("lab4_input.txt", "rt", encoding="utf-8") as fi:
        with open("lab4_output.txt", "wt", encoding="utf-8") as fo:
            # Пропускаем строки заголовка
            for _ in range(3):
                fi.readline()

            n = int(fi.readline().strip())
            if n > 30:
                n = 30
            elif n < 5:
                n = 5

            mas = []
            for i in range(n):
                mas.append(random.uniform(-5.0, 5.0))

            fo.write("ЛАБОРАТОРНАЯ РАБОТА №4\n")
            fo.write("=" * 60 + "\n")
            fo.write(f"Размер массива: N = {n}\n\n")

            fo.write("1. Исходный массив:\n")
            fo.write("-" * 40 + "\n")
            for i in range(n):
                fo.write("{0:8.3f}".format(mas[i]))
                if (i + 1) % 5 == 0 or i == n - 1:
                    fo.write("\n")

            negative_sum = 0.0
            for element in mas:
                if element < 0:
                    negative_sum += element

            max_index = 0
            min_index = 0
            for i in range(1, n):
                if mas[i] > mas[max_index]:
                    max_index = i
                if mas[i] < mas[min_index]:
                    min_index = i

            product_between = 1.0
            start_index = min(min_index, max_index) + 1
            end_index = max(min_index, max_index)

            if end_index - start_index > 0:
                for i in range(start_index, end_index):
                    product_between *= mas[i]
            else:
                product_between = 0.0

            fo.write("\n2. Результаты обработки:\n")
            fo.write("-" * 40 + "\n")
            fo.write("Сумма отрицательных элементов: {0:8.3f}\n".format(negative_sum))
            fo.write("Максимальный элемент: {0:8.3f} (индекс {1})\n".format(mas[max_index], max_index))
            fo.write("Минимальный элемент:  {0:8.3f} (индекс {1})\n".format(mas[min_index], min_index))
            fo.write("Произведение элементов между max и min: {0:8.3f}\n".format(product_between))

            if end_index - start_index > 0:
                fo.write("Элементы между индексами {0}-{1}:\n".format(start_index, end_index - 1))
                for i in range(start_index, end_index):
                    fo.write("{0:8.3f}".format(mas[i]))
                fo.write("\n")

            sorted_mas = mas.copy()
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if sorted_mas[i] > sorted_mas[j]:
                        sorted_mas[i], sorted_mas[j] = sorted_mas[j], sorted_mas[i]

            fo.write("\n3. Отсортированный массив:\n")
            fo.write("-" * 40 + "\n")
            for i in range(n):
                fo.write("{0:8.3f}".format(sorted_mas[i]))
                if (i + 1) % 5 == 0 or i == n - 1:
                    fo.write("\n")

            fo.write("\n" + "=" * 60 + "\n")

    print("Результаты записаны в lab4_output.txt")


if __name__ == "__main__":
    main()