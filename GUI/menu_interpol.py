import tkinter as tk
import tkinter.ttk as ttk

from GUI.utils import *


class InterpolationMenu(tk.Toplevel):
    def __init__(self, master, toolbar, plotspace):
        super().__init__(master)
        self.master = master
        self.toolbar = toolbar
        self.plotspace = plotspace
        self.title("Interpolation")
        self.geometry("300x300")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.close)

        self.label = ttk.Label(
            self, text="Choisir le degrés du polynôme d'interpolation"
        )
        self.label.pack(pady=10)

        self.deg = tk.IntVar()
        self.entry = ttk.Entry(
            self,
            text="Degrès d'interpolation",
            textvariable=self.deg,
        )
        self.entry.pack(pady=10)

        self.button = ttk.Button(self, text="Valider", command=self.interpolation)
        self.button.pack(pady=10)

        self.entry.bind("<Return>", self.interpolation)

    def interpolation(self, event=None):
        try:
            isinstance(self.deg.get(), int)
        except:
            self.label.config(text="Veuillez entrer un entier")
        else:
            self.plotspace.interpolation(self.deg.get())
            self.close()

    def close(self):
        self.destroy()
