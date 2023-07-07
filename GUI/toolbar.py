import tkinter as tk
import tkinter.ttk as ttk

from GUI.drop_menu import DropMenu
from GUI.menuhandler import MenuHandler


class Toolbar(tk.Frame):
    def __init__(self, master, plotspace):
        super().__init__(master)
        self.master = master
        self.plotspace = plotspace

        self.file = DropMenu("Fichier", self)
        self.file.button.pack(side="left", padx=(1, 0))

        self.tools = DropMenu("Outils", self)
        self.tools.button.pack(side="left", padx=(1, 0))

    def link_to(self, plotspace):
        self.plotspace = plotspace
        self.menu = MenuHandler(self.master, self, self.plotspace)

        self.file.add_commands(
            [
                "Nouveau (Ctrl + N)",
                "Enregistrer plot (Ctrl + S)",
                "Nettoyer",
                "Quitter",
            ],
            [
                self.menu.createCurveMenu,
                self.plotspace.save,
                self.plotspace.clear,
                self.on_closing,
            ],
        )

        self.tools.add_commands(
            [
                "Paliers",
                "Rég linéaire",
                "Interpolation poly (Ctrl + I)",
            ],
            [
                self.menu.createStageMenu,
                self.plotspace.LinearRegression,
                self.menu.createInterpolationMenu,
            ],
        )

        self.master.bind("<Control-n>", self.menu.createCurveMenu)
        self.master.bind("<Control-i>", self.menu.createInterpolationMenu)
        self.master.bind("<Control-s>", self.plotspace.save)

    def on_closing(self):
        if tk.messagebox.askokcancel(
            "Quitter", "Toute progression non sauvegardée sera perdue."
        ):
            self.master.destroy()
