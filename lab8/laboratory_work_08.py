"""
Лабораторная работа №8: GUI, модуль Tkinter
Вариант 1: Графики функций, заданных рядами Тейлора и аналитически.
Автор: DeepSeek
"""

import tkinter as tk
from tkinter.messagebox import showwarning, askyesno
from math import log

# ========================== Глобальные переменные ==========================
Kp = 0.7  # коэффициент размера окна (70% экрана)
root = tk.Tk()
root.title("Графики функций (Вариант 1)")

# Размеры полотна
MaxX = int(root.winfo_screenwidth() * Kp)
MaxY = int(root.winfo_screenheight() * Kp)

# Пользовательские координаты
Xmin, Xmax = -10.0, 10.0
Ymin, Ymax = -5.0, 5.0
dY = 1.0  # смещение второй функции
dX = 1.0  # шаг меток

# Масштабные коэффициенты
Kx = MaxX / abs((Xmax - Xmin))
Ky = MaxY / abs((Ymax - Ymin))

# Идентификаторы для линий курсора
ID1 = 0
ID2 = 0

# ========================== Функции вычисления ==========================
def series_y(x, eps=1e-6):
    """
    Вычисление функции y(x) через ряд Тейлора.
    Ряд: 2 * sum(1 / ((2*n+1) * x^(2*n+1))) для |x| > 1
    """
    if abs(x) <= 1:
        return None  # ряд расходится при |x| <= 1
    n = 0
    term = 1 / ((2 * n + 1) * x ** (2 * n + 1))
    total = term
    while abs(term) > eps:
        n += 1
        term = 1 / ((2 * n + 1) * x ** (2 * n + 1))
        total += term
    return 2 * total

def func_z(x, b):
    """
    Вычисление функции z(x) = ln((x+1)/(x-1)) + b.
    Область определения: x > 1 или x < -1.
    """
    if abs(x) <= 1:
        return None
    return log((x + 1) / (x - 1)) + b

def get_y_values():
    """Возвращает список точек (x, y) для первой функции."""
    points = []
    x = Xmin
    step = 1 / Kx  # шаг в пользовательских единицах
    while x <= Xmax:
        y = series_y(x)
        if y is not None:
            points.append((x, y))
        x += step
    return points

def get_z_values(b):
    """Возвращает список точек (x, z) для второй функции."""
    points = []
    x = Xmin
    step = 1 / Kx
    while x <= Xmax:
        z = func_z(x, b)
        if z is not None:
            points.append((x, z))
        x += step
    return points

# ========================== GUI-функции ==========================
def get_data():
    """Считывает данные из полей ввода."""
    global Xmin, Xmax, Ymin, Ymax, dX, dY, Kx, Ky
    try:
        Xmin = float(ent_xmin.get())
        Xmax = float(ent_xmax.get())
        Ymin = float(ent_ymin.get())
        Ymax = float(ent_ymax.get())
        dX = float(ent_dx.get())
        dY = float(ent_dy.get())
    except ValueError:
        showwarning("Ошибка", "Некорректный ввод чисел")
        return False

    if Xmin >= Xmax or Ymin >= Ymax or dX <= 0:
        showwarning("Ошибка", "Должны выполняться:\nXmax > Xmin\nYmax > Ymin\nШаг > 0")
        return False

    Kx = MaxX / abs((Xmax - Xmin))
    Ky = MaxY / abs((Ymax - Ymin))
    return True

def plot_axes():
    """Рисует координатные оси с метками."""
    cv.delete("all")
    # Прямоугольник области графика
    cv.create_rectangle(5, 5, MaxX - 5, MaxY - 5, outline="green", width=2)

    # Метки по оси Y
    y = Ymin
    while y <= Ymax:
        y_pix = MaxY - Ky * (y - Ymin)
        cv.create_line(0, y_pix, 10, y_pix, fill='black', width=2)
        cv.create_line(MaxX - 10, y_pix, MaxX, y_pix, fill='black', width=2)
        cv.create_text(20, y_pix, text=f"{y:.1f}", anchor=tk.W)
        cv.create_text(MaxX - 20, y_pix, text=f"{y:.1f}", anchor=tk.E)
        y += dX

    # Метки по оси X
    x = Xmin
    while x <= Xmax:
        x_pix = Kx * (x - Xmin)
        cv.create_line(x_pix, MaxY, x_pix, MaxY - 10, fill='black', width=2)
        cv.create_line(x_pix, 0, x_pix, 10, fill='black', width=2)
        cv.create_text(x_pix, MaxY - 20, text=f"{x:.1f}", anchor=tk.N)
        cv.create_text(x_pix, 20, text=f"{x:.1f}", anchor=tk.S)
        x += dX

def draw_graph(event=None):
    """Рисует графики функций."""
    if not get_data():
        return
    plot_axes()

    # Первая функция (синий)
    points_y = get_y_values()
    pix_points = [(Kx * (x - Xmin), MaxY - Ky * (y - Ymin)) for x, y in points_y]
    cv.create_line(pix_points, fill='blue', width=2)

    # Вторая функция (красный)
    try:
        b = float(ent_dy.get())
    except ValueError:
        b = 0.0
    points_z = get_z_values(b)
    pix_points = [(Kx * (x - Xmin), MaxY - Ky * (z - Ymin)) for x, z in points_z]
    cv.create_line(pix_points, fill='red', width=2)

def show_xy(event):
    """Выводит координаты мыши и рисует перекрестие."""
    global ID1, ID2
    x_pix, y_pix = event.x, event.y
    x_user = Xmin + x_pix / Kx
    y_user = Ymin + (MaxY - y_pix) / Ky

    ent_x.delete(0, tk.END)
    ent_y.delete(0, tk.END)
    ent_x.insert(0, f"{x_user:.2f}")
    ent_y.insert(0, f"{y_user:.2f}")

    cv.delete(ID1)
    cv.delete(ID2)
    ID1 = cv.create_line(0, y_pix, MaxX, y_pix, dash=(3, 5))
    ID2 = cv.create_line(x_pix, 0, x_pix, MaxY, dash=(3, 5))

def final(event=None):
    """Завершает программу."""
    if askyesno("Выход", "Завершить работу?"):
        root.destroy()

def window_deleted():
    """Обработчик закрытия окна."""
    final()

# ========================== GUI-виджеты ==========================
root.resizable(False, False)
root.protocol('WM_DELETE_WINDOW', window_deleted)

# Полотно для графики
cv = tk.Canvas(root, width=MaxX, height=MaxY, bg="white")
cv.grid(row=0, columnspan=10)
cv.bind('<Button-1>', show_xy)

# Метки и поля ввода
labels = [
    ("X:", 1, 0), ("Y:", 2, 0),
    ("Xmin:", 1, 2), ("Xmax:", 1, 4),
    ("Ymin:", 2, 2), ("Ymax:", 2, 4),
    ("Шаг:", 1, 6), ("b (смещ.):", 2, 6)
]

entries = []
for text, row, col in labels:
    lbl = tk.Label(root, text=text, width=10, fg="blue", font="Ubuntu 12")
    lbl.grid(row=row, column=col, sticky='e')
    ent = tk.Entry(root, width=8, font="Ubuntu 12")
    ent.grid(row=row, column=col + 1)
    entries.append(ent)

ent_x, ent_y, ent_xmin, ent_xmax, ent_ymin, ent_ymax, ent_dx, ent_dy = entries

# Заполнение начальными значениями
ent_xmin.insert(0, str(Xmin))
ent_xmax.insert(0, str(Xmax))
ent_ymin.insert(0, str(Ymin))
ent_ymax.insert(0, str(Ymax))
ent_dx.insert(0, str(dX))
ent_dy.insert(0, str(dY))
ent_x.insert(0, "0.00")
ent_y.insert(0, "0.00")

# Кнопки
btn_draw = tk.Button(root, width=15, text="Рисовать", bg="#ccc")
btn_draw.grid(row=1, column=8, columnspan=2)
btn_draw.bind("<Button-1>", draw_graph)

btn_exit = tk.Button(root, width=15, text="Выход", bg="#ccc")
btn_exit.grid(row=2, column=8, columnspan=2)
btn_exit.bind("<Button-1>", final)

# ========================== Запуск ==========================
root.mainloop()