import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import askokcancel
from tkinter import filedialog
from GUI.utils import *
from GUI.toolbar import *
from GUI.plotspace import *
from GUI.sidebar import *

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class App:
    def __init__(self, master):
        self.master = master
        self.master.state("zoomed")
        self.master.columnconfigure(0, weight=3)
        self.master.columnconfigure(1, weight=1)

        self.toolbar = Toolbar(self.master, None)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.plotspace = Plotspace(self.master, None)
        self.plotspace.grid(row=1, column=0)

        self.sidebar = Sidebar(self.master, self.plotspace)
        self.sidebar.grid(row=1, column=1, sticky="ns")

        self.toolbar.link_to(self.plotspace)
        self.plotspace.link_to(self.sidebar)

        self.master.bind("<Control-q>", on_closing)


def on_closing(event=None):
    if askokcancel(
        "Quitter", "Toute progression non sauvegardée sera perdue.", icon="warning"
    ):
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.title("ThermoGraph")
    root.protocol("WM_DELETEs_WINDOW", on_closing)
    root.mainloop()
