import random
def create_matrix(rows, cols, a, b):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(a, b))
        matrix.append(row)
    return matrix
def print_matrix(matrix, title="Матрица:"):
    print(f"\n{title}")
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    for i in range(rows):
        for j in range(cols):
            print(f"{matrix[i][j]:4d}", end=" ")
        print()
def count_rows_without_zero(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    for i in range(rows):
        has_zero = False
        for j in range(cols):
            if matrix[i][j] == 0:
                has_zero = True
                break
        if not has_zero:
            count += 1
    return count
def find_max_repeating_number(matrix):
    # Создаем словарь для подсчета частоты чисел
    frequency = {}
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Подсчитываем частоту каждого числа
    for i in range(rows):
        for j in range(cols):
            num = matrix[i][j]
            frequency[num] = frequency.get(num, 0) + 1
    # Ищем максимальное число, встречающееся более одного раза
    max_repeating = None
    for num, count in frequency.items():
        if count > 1:
            if max_repeating is None or num > max_repeating:
                max_repeating = num
    return max_repeating
def main():
    # Ввод размеров матрицы
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
    # Создание матрицы
    matrix = create_matrix(rows, cols, -10, 10)
    # Вывод исходной матрицы
    print_matrix(matrix, "Исходная матрица:")
    # 1. Количество строк без нулевых элементов
    rows_without_zero = count_rows_without_zero(matrix)
    print(f"\n1. Количество строк без нулевых элементов: {rows_without_zero}")
    # 2. Максимальное значение из чисел, встречающихся более одного раза
    max_repeating = find_max_repeating_number(matrix)
    if max_repeating is not None:
        print(f"2. Максимальное число, встречающееся более одного раза: {max_repeating}")
        # Дополнительная информация: покажем, где встречается это число
        print("   Позиции этого числа в матрице:")
        rows_count = len(matrix)
        cols_count = len(matrix[0]) if rows_count > 0 else 0
        positions = []
        for i in range(rows_count):
            for j in range(cols_count):
                if matrix[i][j] == max_repeating:
                    positions.append((i, j))
        for pos in positions:
            print(f"      Строка {pos[0]}, столбец {pos[1]}")
    else:
        print("2. В матрице нет чисел, встречающихся более одного раза")
if __name__ == "__main__":
    main()