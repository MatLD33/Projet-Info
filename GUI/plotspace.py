import tkinter as tk
import tkinter.ttk as ttk
from GUI.canvas import MyCanvas

import matplotlib
import numpy as np

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from tkinter import filedialog

from GUI.utils import *


class Plotspace(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#dddddd")
        self.master = master
        self.reinit()

        self.fig = Figure(dpi=100)
        self.canvas = MyCanvas(self.fig, self, self.master)

    def reinit(self):
        self.image_list = []
        self.image_tk_list = []
        self.current = 0
        self.scale = []
        self.current_image = None
        self.mode = "BLANK"

    def add_curve(self, path):
        self.reinit()
        self.image_list.append(path)
        # self.image_tk_list.append(tk.PhotoImage(file="Data/" + path))
        self.current = len(self.image_list) - 1

        x, data_to_plot, val = create_data(path, 2)
        self.canvas.abs = x
        self.canvas.ord = val

        self.fig.clear()
        self.sub = self.fig.add_subplot(111)
        self.sub.plot(self.canvas.abs, self.canvas.ord)
        self.sub.set_xlabel("Balayage")
        self.sub.set_ylabel(data_to_plot)
        self.sub.grid()
        self.canvas.draw()
        self.canvas.get_tk_widget().grid()

    def interpolation(self, deg):
        if self.canvas.poly is not None:
            self.sub.lines.pop(1)
        self.canvas.poly = polynomial_interpolation(
            self.canvas.abs, self.canvas.ord, deg
        )

        coef = self.canvas.poly.coef
        coef = np.round(coef, 3)
        self.polystring = ""
        for i in range(len(coef)):
            self.polystring += f"{coef[i]}x^{len(coef)-i-1} + "
        self.polystring = self.polystring[:-3]

        self.sub.plot(
            self.canvas.abs,
            self.canvas.poly(self.canvas.abs),
            "r",
            label=f"Interpolation : {self.polystring}",
        )
        self.sub.legend()
        self.canvas.draw()
        self.canvas.get_tk_widget().grid()

    def LinearRegression(self):
        self.interpolation(1)

    def clear(self):
        self.fig.clear()

    def save(self, event=None):
        name = filedialog.asksaveasfilename()
        self.fig.savefig(name)
