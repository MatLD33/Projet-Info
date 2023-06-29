import tkinter as tk
import tkinter.ttk as ttk
from GUI.canvas import MyCanvas

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from GUI.utils import *


class Plotspace(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.reinit()
        self.mode = "BLANK"

        self.fig = Figure(dpi=100)
        self.canvas = MyCanvas(self.fig, self, self.master)

    def reinit(self):
        self.image_list = []
        self.image_tk_list = []
        self.current = 0
        self.scale = []
        # self.offset = []
        self.current_image = None
        self.mode = "BLANK"

    def add_curve(self, path):
        self.reinit()
        self.image_list.append(path)
        # self.image_tk_list.append(tk.PhotoImage(file="Data/" + path))
        self.current = len(self.image_list) - 1

        x, data_to_plot, val = create_data(path, 2)
        self.fig.clear()
        p1 = self.fig.add_subplot(111)
        p1.plot(x, val)
        p1.set_xlabel("Balayage")
        p1.set_ylabel(data_to_plot)
        p1.grid()
        self.canvas.draw()
        self.canvas.get_tk_widget().grid()