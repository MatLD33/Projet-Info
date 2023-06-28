import tkinter as tk
import tkinter.ttk as ttk

from GUI.drop_menu import DropMenu


class Toolbar(tk.Frame):
    def __init__(self, parent, plotspace):
        super().__init__(parent)
        self.parent = parent
        self.plotspace = plotspace

        self.file = DropMenu("Fichier", self)
        self.file.button.pack(side="left", padx=(1, 0))

        self.tools = DropMenu("Outils", self)
        self.tools.button.pack(side="left", padx=(1, 0))

    def link_to(self, plotspace):
        self.plotspace = plotspace

        self.file.add_commands(
            ["Nouveau", "Enregistrer", "Quitter"],
            [
                lambda: print("to bind"),
                lambda: print("to bind"),
                self.on_closing(self.parent),
            ],
        )

        self.tools.add_commands(
            ["Annuler (Ctrl + Z)", "Paliers"],
            [lambda: print("to bind"), lambda: print("to bind")],
        )

    def open_file(self, event=None):
        pass

    def on_closing(self, parent):
        if tk.messagebox.askokcancel(
            "Quitter", "Toute progression non sauvegardée sera perdue."
        ):
            parent.destroy()
