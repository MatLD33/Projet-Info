import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from GUI.utils import *
from GUI.toolbar import *
from GUI.plotspace import *

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x500")

        self.toolbar = Toolbar(self.master, None)
        self.toolbar.grid(row=0, column=0, columnspan=3, sticky="ew")

        self.plotspace = Plotspace(self.master)
        self.plotspace.grid(row=1, column=1, sticky="ns")

        self.toolbar.link_to(self.plotspace)

        # shortcuts binding
        self.master.bind("<Control-n>", self.toolbar.open_file)

    def on_closing(self):
        if tk.messagebox.askokcancel(
            "Quitter", "Toute progression non sauvegardée sera perdue."
        ):
            root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.title("ThermoGraph")
    root.protocol("WM_DELETEs_WINDOW", app.on_closing)
    root.mainloop()
