import tkinter as tk
import tkinter.ttk as ttk

from GUI.plotspace import *
from GUI.utils import *


class CurveMenu(tk.Toplevel):
    def __init__(self, master, toolbar, plotspace):
        super().__init__(master)
        self.master = master
        self.toolbar = toolbar
        self.plotspace = plotspace
        self.title("Coube à afficher")
        self.geometry("250x200")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.close)

        self.donnee_x = tk.BooleanVar()
        self.checkb = ttk.Checkbutton(
            self,
            text="Donnée en abscisse ?",
            variable=self.donnee_x,
            command=self.check,
        )
        self.checkb.pack(pady=10)

        self.label_o = ttk.Label(self, text="Donnée en ordonnée :")
        self.label_o.place(x=10, y=50)

        self.button_o = ttk.Button(self, text="Choisir", command=self.add_curve)
        self.button_o.place(x=150, y=50)

        self.label_a = ttk.Label(self, text="Donnée en abscisse :")
        self.label_a.place(x=10, y=100)
        self.label_a_check = False

        self.button_a = ttk.Button(self, text="Choisir", command=self.add_curve)
        self.button_a.place(x=150, y=100)
        self.button_a_check = False

        self.button_v = ttk.Button(self, text="Valider", command=self.close)
        self.button_v.place(x=90, y=150)

    def check(self):
        if self.donnee_x.get():
            if self.label_a_check:
                self.label_a.place(x=10, y=100)
                self.label_a_check = False
                self.button_a.place(x=150, y=100)
                self.button_a_check = False
        else:
            self.label_a.place_forget()
            self.label_a_check = True
            self.button_a.place_forget()
            self.button_a_check = True

    def add_curve(self):
        path = tk.filedialog.askopenfilename(initialdir="Data")
        path_end = "Data/" + path.split("/")[-1]

        self.plotspace.add_curve(path_end)
        self.destroy()

    def close(self):
        self.destroy()
