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
        self.init_lab.grid(row=0, column=0, columnspan=2)

        self.xlab = ttk.Label(self, text=f"X : None", font=("Arial", 12))
        self.xlab.grid(row=1, column=0, columnspan=2)

        self.ylab = ttk.Label(self, text=f"Y : None", font=("Arial", 12))
        self.ylab.grid(row=2, column=0, columnspan=2)

        self.polylab = ttk.Label(
            self, text=f"Polynôme interpolateur : \n 0", font=("Arial", 12)
        )
        self.polylab.grid(row=4, column=0, columnspan=2)

        self.matrixlab = ttk.Label(
            self, text=f"Matrice des paliers :", font=("Arial", 14)
        )
        self.matrixlab.grid(row=6, column=0)

        self.save_button = ttk.Button(self, text="Enregistrer", command=self.save)
        self.save_button.grid(row=6, column=1)

    def x_writer(self, x_val):
        self.xlab.config(text=f"X : {x_val}")

    def y_writer(self, y_val):
        self.ylab.config(text=f"Y : {y_val}")

    def poly_writer(self, poly):
        self.polylab.config(text=f"Polynôme interpolateur : \n {poly}")

    def matrix_writer(self, matrix, times):
        self.matrix = tk.Text(self)
        self.matrix.grid(row=7, column=0, columnspan=2)
        nb_stages = len(matrix)
        ind = np.arange(nb_stages)
        df = pd.DataFrame(
            matrix,
            index=ind,
            columns=[
                "Debut",
                "Fin",
                "Moyenne",
                "Variance",
            ],
        )

        df["tps init"] = times[:, 0]
        df["tps fin"] = times[:, 1]
        df["Durée"] = times[:, 2]

        self.matrix.insert(tk.END, df)

    def save(self):
        pass

    def clear(self):
        self.xlab.config(text=f"X : None")
        self.ylab.config(text=f"Y : None")
        self.polylab.config(text=f"Polynôme interpolateur : \n 0")
        self.matrixlab.config(text=f"Matrice des paliers :")
