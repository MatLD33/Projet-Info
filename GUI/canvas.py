import tkinter as tk
import tkinter.ttk as ttk


class MyCanvas(tk.Canvas):
    def __init__(self, plotspace, master, **kwargs):
        super().__init__(master, **kwargs)
        self.plotpsace = plotspace
