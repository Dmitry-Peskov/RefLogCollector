import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Сборщик log-файлов ПК "Спринтер"')
        self.root.resizable(False, False)
        self.root.geometry("800x400+600+300")  # ширина, высота, отступ слева, отступ сверху

    def draw_widgets(self):
        w = GUI(parent=self.root)
        w.label_1.grid(row=0, column=0)
        w.dipost_path.grid(row=0, column=1)
        w.btn_dipost_path.grid(row=0, column=2)
        w.label_2.grid(row=1, column=0)
        w.save_path.grid(row=1, column=1)
        w.btn_save_path.grid(row=1, column=2)

    def run(self):
        self.root.mainloop()


class GUI:
    def __init__(self, parent: tk.Tk):
        self.label_1 = tk.Label(parent, text='Каталог установки программы:')
        self.dipost_path = tk.Entry(parent, width=50, textvariable=tk.StringVar(value='C:\\Dipost'))
        self.btn_dipost_path = tk.Button(parent, text='Выбрать папку')
        self.label_2 = tk.Label(parent, text='Каталог сохранения log файлов:')
        self.save_path = tk.Entry(parent, width=50, textvariable=tk.StringVar(value='C:\\Dipost'))
        self.btn_save_path = tk.Button(parent, text='Выбрать папку')

