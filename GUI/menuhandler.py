import tkinter as tk
import tkinter.ttk as ttk

from GUI.menu_curve import CurveMenu
from GUI.menu_interpol import InterpolationMenu


class MenuHandler:
    def __init__(self, master, toolbar, plotspace):
        self.master = master
        self.toolbar = toolbar
        self.plotspace = plotspace

    def createCurveMenu(self, event=None):
        CurveMenu(self.master, self.toolbar, self.plotspace)

    def createInterpolationMenu(self):
        InterpolationMenu(self.master, self.toolbar, self.plotspace)
