import tkinter as tk
import tkinter.ttk as ttk
from GUI.canvas import MyCanvas

import matplotlib
import numpy as np

matplotlib.use("TkAgg")
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from tkinter import filedialog

from GUI.utils import *


class Plotspace(tk.Frame):
    def __init__(self, master, sidebar):
        super().__init__(master, bg="#dddddd")
        self.master = master
        self.sidebar = sidebar
        self.reinit()

        self.fig = Figure(dpi=100)
        self.canvas = MyCanvas(self.fig, self, self.master)

        # self.navbar = NavigationToolbar2Tk(self.canvas, self.master)
        # self.navbar.update()

        self.canvas.get_tk_widget().grid()

    def reinit(self):
        self.image_list = []
        self.image_tk_list = []
        self.current = 0
        self.scale = []
        self.current_image = None
        self.mode = "BLANK"

    def link_to(self, sidebar):
        self.sidebar = sidebar

    def set_y(self, path):
        x, data_to_plot, val = create_data(path, 2)
        _, _, times = create_data(path, 1, data_type="time")
        self.canvas.times = times
        self.canvas.ord = val
        self.canvas.abs = x
        self.canvas.ylab = data_to_plot
        self.canvas.xlab = "Balayage"

    def set_x(self, path):
        x, data_to_plot, val = create_data(path, 2)
        self.canvas.abs = val
        self.canvas.xlab = data_to_plot

    def add_curve(self):
        self.reinit()
        # self.image_list.append(path)
        # # self.image_tk_list.append(tk.PhotoImage(file="Data/" + path))
        # self.current = len(self.image_list) - 1

        self.fig.clear()
        self.sub = self.fig.add_subplot(111)
        self.sub.plot(self.canvas.abs, self.canvas.ord)
        self.sub.set_xlabel(self.canvas.xlab)
        self.sub.set_ylabel(self.canvas.ylab)
        self.sidebar.x_writer(self.canvas.xlab)
        self.sidebar.y_writer(self.canvas.ylab)
        self.sub.grid()
        self.canvas.draw()
        self.canvas.get_tk_widget().grid()

    def interpolation(self, deg):
        if self.canvas.poly is not None:
            self.sub.lines.pop(1)
        self.canvas.poly, coef = polynomial_interpolation(
            self.canvas.abs, self.canvas.ord, deg
        )
        print(self.canvas.poly)
        # coef = np.round(coef, 3)
        self.polystring = ""
        for i in range(len(coef)):
            self.polystring += f"{coef[i]}x^{len(coef) - i -1} + "
        self.polystring = self.polystring[:-3]

        self.sidebar.poly_writer(self.polystring)

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
        self.sidebar.clear()

    def save(self, event=None):
        name = filedialog.asksaveasfilename()
        self.fig.savefig(name)

    def set_stage(self, w_size, precision):
        stage_matrix, time_matrix = detect_stable_stage(
            self.canvas.ord, self.canvas.times, precision, w_size
        )
        self.sidebar.matrix_writer(stage_matrix, time_matrix)
