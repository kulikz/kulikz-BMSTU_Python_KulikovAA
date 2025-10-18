import random
def main():
    n = int(input("Введите количество элементов массива (N<=30): "))
    if n > 30:
        n = 30
    elif n < 5:
        n = 5
    mas = []
    for i in range(n):
        mas.append(random.uniform(-5.0, 5.0))
    print("\nНачальное состояние массива:")
    for i in range(n):
        print("{0:8.3f}".format(mas[i]), end=" ")
    print()
    # 1. Сумма отрицательных элементов
    negative_sum = 0.0
    for element in mas:
        if element < 0:
            negative_sum += element
    # 2. Поиск индексов максимального и минимального элементов
    max_index = 0
    min_index = 0
    for i in range(1, n):
        if mas[i] > mas[max_index]:
            max_index = i
        if mas[i] < mas[min_index]:
            min_index = i
    # Произведение элементов между максимальным и минимальным
    product_between = 1.0
    start_index = min(min_index, max_index) + 1
    end_index = max(min_index, max_index)
    if end_index - start_index > 0:
        for i in range(start_index, end_index):
            product_between *= mas[i]
    else:
        product_between = 0.0  # Если между элементами нет других элементов
    # Сортировка массива по возрастанию
    sorted_mas = mas.copy()
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sorted_mas[i] > sorted_mas[j]:
                sorted_mas[i], sorted_mas[j] = sorted_mas[j], sorted_mas[i]
    # Вывод результатов
    print("\nРезультаты:")
    print(f"1. Сумма отрицательных элементов: {negative_sum:8.3f}")
    print(f"2. Произведение элементов между максимальным и минимальным: {product_between:8.3f}")
    print("\nОтсортированный массив:")
    for i in range(n):
        print("{0:8.3f}".format(sorted_mas[i]), end=" ")
    print()
    print(f"   Максимальный элемент: {mas[max_index]:8.3f} (индекс {max_index})")
    print(f"   Минимальный элемент:  {mas[min_index]:8.3f} (индекс {min_index})")
    print(f"   Элементы между ними (индексы {start_index}-{end_index - 1}): ", end="")
    if end_index - start_index > 0:
        for i in range(start_index, end_index):
            print(f"{mas[i]:8.3f}", end=" ")
    else:
        print("нет элементов")
    print()
if __name__ == "__main__":
    main()