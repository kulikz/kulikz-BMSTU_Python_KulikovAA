from tkinter import *
from tkinter import messagebox
from math import log
from base_graph_app import BaseGraphApp


class GraphApp(BaseGraphApp):
    def __init__(self):
        super().__init__("Графики функций - Вариант 1")

    def y_function(self, x, eps=1e-6):
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

    def z_function(self, x, b):
        if abs(x) <= 1:
            return None
        ratio = (x + 1) / (x - 1)
        if ratio <= 0:
            return None
        return log(ratio) + b

    def get_data(self):
        try:
            self.Xmin = float(self.ent_xmin.get())
            self.Xmax = float(self.ent_xmax.get())
            self.Ymin = float(self.ent_ymin.get())
            self.Ymax = float(self.ent_ymax.get())
            self.dX = float(self.ent_step.get())
            self.b_value = float(self.ent_b.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат чисел")
            return False

        if self.Xmin >= self.Xmax or self.Ymin >= self.Ymax or self.dX <= 0:
            messagebox.showerror("Ошибка", "Некорректные границы или шаг")
            return False

        self.Kx = self.MaxX / (self.Xmax - self.Xmin)
        self.Ky = self.MaxY / (self.Ymax - self.Ymin)
        return True

    def to_pixel(self, x, y):
        if y is None:
            return None
        xp = self.Kx * (x - self.Xmin)
        yp = self.MaxY - self.Ky * (y - self.Ymin)
        return (xp, yp)

    def draw_axes(self):
        self.cv.delete("axes")
        ox = self.to_pixel(0, 0)
        if ox:
            self.cv.create_line(0, ox[1], self.MaxX, ox[1], fill="black", tags="axes")
            self.cv.create_line(ox[0], 0, ox[0], self.MaxY, fill="black", tags="axes")

        x = self.Xmin
        while x <= self.Xmax:
            pos = self.to_pixel(x, 0)
            if pos:
                self.cv.create_line(pos[0], pos[1] - 5, pos[0], pos[1] + 5, fill="black", tags="axes")
                if abs(x) > 1e-9:
                    self.cv.create_text(pos[0], pos[1] + 15, text=f"{x:.1f}", anchor=N, tags="axes")
            x += self.dX

        y = self.Ymin
        while y <= self.Ymax:
            pos = self.to_pixel(0, y)
            if pos:
                self.cv.create_line(pos[0] - 5, pos[1], pos[0] + 5, pos[1], fill="black", tags="axes")
                if abs(y) > 1e-9:
                    self.cv.create_text(pos[0] - 10, pos[1], text=f"{y:.1f}", anchor=E, tags="axes")
            y += self.dX

    def draw_function(self):
        if not self.get_data():
            return

        self.cv.delete("graph")
        self.draw_axes()

        points_y = []
        points_z = []

        x = self.Xmin
        while x <= self.Xmax:
            if abs(x) > 1:
                y_val = self.y_function(x)
                if y_val is not None and self.Ymin <= y_val <= self.Ymax:
                    points_y.append(self.to_pixel(x, y_val))
                else:
                    if points_y:
                        self.cv.create_line(points_y, fill="blue", smooth=True, tags="graph")
                    points_y = []

            if abs(x) > 1:
                z_val = self.z_function(x, self.b_value)
                if z_val is not None and self.Ymin <= z_val <= self.Ymax:
                    points_z.append(self.to_pixel(x, z_val))
                else:
                    if points_z:
                        self.cv.create_line(points_z, fill="red", smooth=True, tags="graph")
                    points_z = []

            x += 0.01

        if points_y:
            self.cv.create_line(points_y, fill="blue", smooth=True, tags="graph")
        if points_z:
            self.cv.create_line(points_z, fill="red", smooth=True, tags="graph")

    def on_closing(self):
        if messagebox.askokcancel("Выход", "Завершить работу?"):
            self.root.destroy()

    def on_canvas_click(self, event):
        x_user = self.Xmin + event.x / self.Kx
        y_user = self.Ymin + (self.MaxY - event.y) / self.Ky
        self.ent_mouse_x.delete(0, END)
        self.ent_mouse_y.delete(0, END)
        self.ent_mouse_x.insert(0, f"{x_user:.2f}")
        self.ent_mouse_y.insert(0, f"{y_user:.2f}")

    def run(self):
        self.root.title("Графики функций - Вариант 1")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.MaxX = int(self.root.winfo_screenwidth() * 0.8)
        self.MaxY = int(self.root.winfo_screenheight() * 0.8 * 0.7)

        self.cv = Canvas(self.root, width=self.MaxX, height=self.MaxY, bg="white")
        self.cv.grid(row=0, column=0, columnspan=10, padx=5, pady=5)
        self.cv.bind("<Button-1>", self.on_canvas_click)

        self.Xmin, self.Xmax = -5.0, 5.0
        self.Ymin, self.Ymax = -3.0, 3.0
        self.dX = 1.0
        self.b_value = 0.0
        self.Kx = self.MaxX / (self.Xmax - self.Xmin)
        self.Ky = self.MaxY / (self.Ymax - self.Ymin)

        labels = ["X мыши:", "Y мыши:", "Xmin:", "Xmax:", "Ymin:", "Ymax:", "Шаг:", "b:"]
        entries = []
        defaults = ["0", "0", str(self.Xmin), str(self.Xmax), str(self.Ymin), str(self.Ymax), str(self.dX), str(self.b_value)]

        for i, (label, default) in enumerate(zip(labels, defaults)):
            Label(self.root, text=label, width=10).grid(row=1 + i // 4, column=(i % 4) * 2, padx=5, pady=2, sticky=E)
            ent = Entry(self.root, width=10)
            ent.grid(row=1 + i // 4, column=(i % 4) * 2 + 1, padx=5, pady=2, sticky=W)
            ent.insert(0, default)
            entries.append(ent)

        self.ent_mouse_x, self.ent_mouse_y, self.ent_xmin, self.ent_xmax, self.ent_ymin, self.ent_ymax, self.ent_step, self.ent_b = entries

        btn_draw = Button(self.root, text="Рисовать", command=self.draw_function, width=15)
        btn_draw.grid(row=3, column=8, padx=5, pady=5)

        btn_exit = Button(self.root, text="Выход", command=self.on_closing, width=15)
        btn_exit.grid(row=3, column=9, padx=5, pady=5)

        self.draw_function()
        self.root.mainloop()


def main():
    app = GraphApp()
    app.run()


if __name__ == "__main__":
    main()