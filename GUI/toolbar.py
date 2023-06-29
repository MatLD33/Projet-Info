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
            ["Nouveau", "Enregistrer", "Quitter"],
            [
                self.menu.createCurveMenu,
                lambda: print("to bind"),
                self.on_closing,
            ],
        )

        self.tools.add_commands(
            ["Annuler (Ctrl + Z)", "Paliers", "Interpolation"],
            [
                lambda: print("to bind"),
                lambda: print("to bind"),
                lambda: print("to bind"),
            ],
        )

    def open_file(self, event=None):
        pass

    def on_closing(self):
        if tk.messagebox.askokcancel(
            "Quitter", "Toute progression non sauvegardée sera perdue."
        ):
            self.master.destroy()
