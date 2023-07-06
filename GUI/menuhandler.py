import tkinter as tk
import tkinter.ttk as ttk

from GUI.menu_curve import CurveMenu
from GUI.menu_interpol import InterpolationMenu
from GUI.menu_stage import StageMenu


class MenuHandler:
    def __init__(self, master, toolbar, plotspace):
        self.master = master
        self.toolbar = toolbar
        self.plotspace = plotspace

    def createCurveMenu(self, event=None):
        CurveMenu(self.master, self.toolbar, self.plotspace)

    def createInterpolationMenu(self, event=None):
        InterpolationMenu(self.master, self.toolbar, self.plotspace)

    def createStageMenu(self):
        StageMenu(self.master, self.toolbar, self.plotspace)
