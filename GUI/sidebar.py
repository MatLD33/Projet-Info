import tkinter as tk
import tkinter.ttk as ttk

import numpy as np
import pandas as pd


class Sidebar(ttk.Frame):
    def __init__(self, master, plotspace):
        super().__init__(master, borderwidth=10)
        self.plotspace = plotspace
        self.master = master
        self.path = None

        self.init_lab = ttk.Label(self, text="Infos des courbes", font=("Arial", 16))
        self.init_lab.grid(row=0, column=0)

    def x_writer(self, x_val):
        self.xlab = ttk.Label(self, text=f"X : {x_val}", font=("Arial", 12))
        self.xlab.grid(row=1, column=0)

    def y_writer(self, y_val):
        self.ylab = ttk.Label(self, text=f"Y : {y_val}", font=("Arial", 12))
        self.ylab.grid(row=2, column=0)

    def poly_writer(self, poly):
        self.polylab = ttk.Label(
            self, text=f"Polynôme interpolateur : \n {poly}", font=("Arial", 12)
        )
        self.polylab.grid(row=4, column=0)

    def matrix_writer(self, matrix):
        self.matrixlab = ttk.Label(
            self, text=f"Matrice des paliers :", font=("Arial", 14)
        )
        self.matrixlab.grid(row=6, column=0)

        self.matrix = tk.Text(self)
        self.matrix.grid(row=7, column=0)
        nb_stages = len(matrix)
        ind = np.arange(nb_stages)
        df = pd.DataFrame(
            matrix,
            index=ind,
            columns=[
                "Debut (Bal)",
                "Fin (Bal)",
                "Debut (Temps)",
                "Fin (Temps)",
                "Moyenne",
                "Variance",
            ],
        )

        self.matrix.insert(tk.END, df)
