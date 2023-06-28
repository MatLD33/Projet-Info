import tkinter as tk
import tkinter.ttk as ttk
from GUI.canvas import MyCanvas


class Plotspace(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.parent = parent
        self.reinit()
        self.mode = "BLANK"

        self.canvas = MyCanvas(
            self, self.master, bg="#dddddd", borderwidth=0, highlightthickness=0
        )

    def reinit(self):
        self.image_list = []
        self.image_tk_list = []
        self.current = 0
        self.h = []
        self.w = []
        self.scale = []
        # self.offset = []
        self.current_image = None
        self.mode = "BLANK"
