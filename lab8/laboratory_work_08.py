from tkinter import *
from tkinter import messagebox
from math import log


def y_function(x, eps=1e-6):
    if abs(x) <= 1:
        return None
    term = 1 / x
    total = term
    n = 1
    while abs(term) > eps:
        term = term / (x * x * (2 * n + 1) / (2 * n - 1))
        total += term
        n += 1
    return 2 * total


def z_function(x, b):
    if abs(x) <= 1:
        return None
    ratio = (x + 1) / (x - 1)
    if ratio <= 0:
        return None
    return log(ratio) + b


def get_data():
    global Xmin, Xmax, Ymin, Ymax, dX, b_value, Kx, Ky
    try:
        Xmin = float(ent_xmin.get())
        Xmax = float(ent_xmax.get())
        Ymin = float(ent_ymin.get())
        Ymax = float(ent_ymax.get())
        dX = float(ent_step.get())
        b_value = float(ent_b.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный формат чисел")
        return False

    if Xmin >= Xmax or Ymin >= Ymax or dX <= 0:
        messagebox.showerror("Ошибка", "Некорректные границы или шаг")
        return False

    Kx = canvas_width / (Xmax - Xmin)
    Ky = canvas_height / (Ymax - Ymin)
    return True


def to_pixel(x, y):
    if y is None:
        return None
    xp = Kx * (x - Xmin)
    yp = canvas_height - Ky * (y - Ymin)
    return (xp, yp)


def draw_axes():
    cv.delete("axes")
    ox = to_pixel(0, 0)
    if ox:
        cv.create_line(0, ox[1], canvas_width, ox[1], fill="black", tags="axes")
        cv.create_line(ox[0], 0, ox[0], canvas_height, fill="black", tags="axes")

    x = Xmin
    while x <= Xmax:
        pos = to_pixel(x, 0)
        if pos:
            cv.create_line(pos[0], pos[1] - 5, pos[0], pos[1] + 5, fill="black", tags="axes")
            if abs(x) > 1e-9:
                cv.create_text(pos[0], pos[1] + 15, text=f"{x:.1f}", anchor=N, tags="axes")
        x += dX

    y = Ymin
    while y <= Ymax:
        pos = to_pixel(0, y)
        if pos:
            cv.create_line(pos[0] - 5, pos[1], pos[0] + 5, pos[1], fill="black", tags="axes")
            if abs(y) > 1e-9:
                cv.create_text(pos[0] - 10, pos[1], text=f"{y:.1f}", anchor=E, tags="axes")
        y += dX


def draw_function():
    if not get_data():
        return

    cv.delete("graph")
    draw_axes()

    points_y = []
    points_z = []

    x = Xmin
    while x <= Xmax:
        if abs(x) > 1:
            y_val = y_function(x)
            if y_val is not None and Ymin <= y_val <= Ymax:
                points_y.append(to_pixel(x, y_val))
            else:
                if points_y:
                    cv.create_line(points_y, fill="blue", smooth=True, tags="graph")
                points_y = []

        if abs(x) > 1:
            z_val = z_function(x, b_value)
            if z_val is not None and Ymin <= z_val <= Ymax:
                points_z.append(to_pixel(x, z_val))
            else:
                if points_z:
                    cv.create_line(points_z, fill="red", smooth=True, tags="graph")
                points_z = []

        x += 0.01

    if points_y:
        cv.create_line(points_y, fill="blue", smooth=True, tags="graph")
    if points_z:
        cv.create_line(points_z, fill="red", smooth=True, tags="graph")


def on_closing():
    if messagebox.askokcancel("Выход", "Завершить работу?"):
        root.destroy()


def on_canvas_click(event):
    x_user = Xmin + event.x / Kx
    y_user = Ymin + (canvas_height - event.y) / Ky
    ent_mouse_x.delete(0, END)
    ent_mouse_y.delete(0, END)
    ent_mouse_x.insert(0, f"{x_user:.2f}")
    ent_mouse_y.insert(0, f"{y_user:.2f}")


root = Tk()
root.title("Графики функций - Вариант 1")
root.protocol("WM_DELETE_WINDOW", on_closing)

canvas_width = 800
canvas_height = 500
Kp = 0.8
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas_width = int(screen_width * Kp)
canvas_height = int(screen_height * Kp * 0.7)

cv = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
cv.grid(row=0, column=0, columnspan=10, padx=5, pady=5)
cv.bind("<Button-1>", on_canvas_click)

Xmin, Xmax = -5.0, 5.0
Ymin, Ymax = -3.0, 3.0
dX = 1.0
b_value = 0.0
Kx = canvas_width / (Xmax - Xmin)
Ky = canvas_height / (Ymax - Ymin)

labels = ["X мыши:", "Y мыши:", "Xmin:", "Xmax:", "Ymin:", "Ymax:", "Шаг:", "b:"]
entries = []
defaults = ["0", "0", str(Xmin), str(Xmax), str(Ymin), str(Ymax), str(dX), str(b_value)]

for i, (label, default) in enumerate(zip(labels, defaults)):
    Label(root, text=label, width=10).grid(row=1 + i // 4, column=(i % 4) * 2, padx=5, pady=2, sticky=E)
    ent = Entry(root, width=10)
    ent.grid(row=1 + i // 4, column=(i % 4) * 2 + 1, padx=5, pady=2, sticky=W)
    ent.insert(0, default)
    entries.append(ent)

ent_mouse_x, ent_mouse_y, ent_xmin, ent_xmax, ent_ymin, ent_ymax, ent_step, ent_b = entries

btn_draw = Button(root, text="Рисовать", command=draw_function, width=15)
btn_draw.grid(row=3, column=8, padx=5, pady=5)

btn_exit = Button(root, text="Выход", command=on_closing, width=15)
btn_exit.grid(row=3, column=9, padx=5, pady=5)

draw_function()
root.mainloop()