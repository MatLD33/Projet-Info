import tkinter as tk
import tkinter.ttk as ttk

from GUI.menu_curve import CurveMenu


class MenuHandler:
    def __init__(self, master, toolbar, plotspace):
        self.master = master
        self.toolbar = toolbar
        self.plotspace = plotspace

    def createCurveMenu(self):
        CurveMenu(self.master, self.toolbar, self.plotspace)
