import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb

from GUI.plotspace import *
from GUI.utils import *


class StageMenu(tk.Toplevel):
    def __init__(self, master, toolbar, plotspace):
        super().__init__(master)
        self.master = master
        self.toolbar = toolbar
        self.plotspace = plotspace
        self.title("Paliers")
        self.geometry("300x200")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.grab_set()

        self.label = ttk.Label(self, text="Paramètres de la fenêtre")
        self.label.place(x=70, y=20)

        self.label_w = ttk.Label(self, text="Taille de la fenêtre :")
        self.label_w.place(x=10, y=50)

        self.w_size = tk.StringVar()
        self.w_size.set("100")
        self.entry = ttk.Entry(self, textvariable=self.w_size)
        self.entry.place(x=150, y=50)

        self.label_v = ttk.Label(self, text="Seuil de variance :")
        self.label_v.place(x=10, y=100)

        self.v_size = tk.StringVar()
        self.v_size.set("0.1")
        self.entry = ttk.Entry(self, textvariable=self.v_size)
        self.entry.place(x=150, y=100)

        self.button_v = ttk.Button(self, text="Valider", command=self.set_stage)
        self.button_v.place(x=90, y=150)

        self.master.bind("<Return>", self.set_stage)

    def set_stage(self):
        try:
            self.w_size_val = float(self.w_size.get())
            self.v_size_val = float(self.v_size.get())
        except ValueError:
            self.w_size_val = 100
            self.v_size_val = 0.1
            mb.showerror("Erreur", "Veuillez entrer des nombres valides (Ex : 46.7)")
        else:
            self.plotspace.set_stage(self.w_size_val, self.v_size_val)

    def close(self):
        self.grab_release()
        self.destroy()
