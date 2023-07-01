import tkinter as tk
import tkinter.ttk as ttk

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MyCanvas(FigureCanvasTkAgg):
    def __init__(self, figure, plotspace, master):
        super().__init__(figure, master)
        self.plotpsace = plotspace
        self.figure = figure
        self.master = master
        self.abs = []
        self.ord = []
        self.xlab = ""
        self.ylab = ""
        self.poly = None
