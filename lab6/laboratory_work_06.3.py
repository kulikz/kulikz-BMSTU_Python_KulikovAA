# -*- coding: utf-8 -*-
import random


def create_input_file():
    """Создание входного файла с тестовыми данными"""
    with open("lab5_input.txt", "w", encoding="utf-8") as fi:
        fi.write("# Лабораторная работа №5\n")
        fi.write("# строки столбцы\n")
        fi.write("#---\n")
        fi.write("4 5\n")
    print("Создан файл lab5_input.txt")


def main():
    create_input_file()

    with open("lab5_input.txt", "rt", encoding="utf-8") as fi:
        with open("lab5_output.txt", "wt", encoding="utf-8") as fo:
            # Пропускаем строки заголовка
            for _ in range(3):
                fi.readline()

            n, m = map(int, fi.readline().split())

            matr = []
            for i in range(n):
                row = []
                for j in range(m):
                    row.append(random.randint(-10, 10))
                matr.append(row)

            fo.write("ЛАБОРАТОРНАЯ РАБОТА №5\n")
            fo.write("=" * 60 + "\n")
            fo.write(f"Размер матрицы: {n} строк, {m} столбцов\n\n")

            fo.write("1. Исходная матрица:\n")
            fo.write("-" * (m * 5 + 5) + "\n")
            for i in range(n):
                fo.write("Строка {0:2d}: ".format(i))
                for j in range(m):
                    fo.write("{0:4d}".format(matr[i][j]))
                fo.write("\n")

            rows_without_zero = 0
            for i in range(n):
                has_zero = False
                for j in range(m):
                    if matr[i][j] == 0:
                        has_zero = True
                        break
                if not has_zero:
                    rows_without_zero += 1

            frequency = {}
            for i in range(n):
                for j in range(m):
                    num = matr[i][j]
                    frequency[num] = frequency.get(num, 0) + 1

            max_repeating = None
            for num, count in frequency.items():
                if count > 1:
                    if max_repeating is None or num > max_repeating:
                        max_repeating = num

            fo.write("\n2. Результаты обработки:\n")
            fo.write("-" * 40 + "\n")
            fo.write("Количество строк без нулевых элементов: {0}\n".format(rows_without_zero))

            if max_repeating is not None:
                fo.write("Максимальное число, встречающееся более одного раза: {0}\n".format(max_repeating))
                fo.write("Частота повторения: {0} раз(а)\n".format(frequency[max_repeating]))

                fo.write("Позиции этого числа:\n")
                for i in range(n):
                    for j in range(m):
                        if matr[i][j] == max_repeating:
                            fo.write("  Строка {0}, столбец {1}\n".format(i, j))
            else:
                fo.write("В матрице нет чисел, встречающихся более одного раза\n")

            fo.write("\n3. Частотный анализ:\n")
            fo.write("-" * 40 + "\n")
            fo.write("{0:^8} | {1:^10} | {2:^10}\n".format("Число", "Частота", "Процент"))
            fo.write("-" * 40 + "\n")

            total = n * m
            sorted_freq = sorted(frequency.items())
            for num, count in sorted_freq:
                percent = (count / total) * 100
                fo.write("{0:^8} | {1:^10} | {2:^10.1f}\n".format(num, count, percent))

            fo.write("\n" + "=" * 60 + "\n")

    print("Результаты записаны в lab5_output.txt")


if __name__ == "__main__":
    main()