from lecture import *
import tkinter as tk
from tkinter import filedialog

import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
import matplotlib.pyplot as plt

def quit_me():
    root.quit()
    root.destroy()

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", quit_me)
root.title("File Selector")
root.geometry("700x400")

label = tk.Label(root, text="Choose your file")
label.pack()

def plot_csv2(path):
    data = pd.read_csv(path, index_col="Bal",delimiter=";")
    columns = data.columns
    data_to_plot = columns[2]
    
    val = str_to_float_v(data[data_to_plot].values)
    figure = Figure(figsize=(5,5), dpi=100)
    p1 = figure.add_subplot(111)

    p1.plot(val)
    plt.figure()
    plt.plot(val)
    plt.xlabel("Balayage")
    plt.ylabel(data_to_plot)
    plt.grid()

    try:
        plt.savefig('Plot/'+new_name(path[5:],'png'))
    except FileNotFoundError:
        os.mkdir("Plot")
        plt.savefig('Plot/'+new_name(path[5:],'png'))
    
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

def select_file():
    file_path = filedialog.askopenfilename(initialdir="Data")
    L = file_path.split("/")
    file_path_fin = "Data/" + L[-1]
    plot_csv2(file_path_fin)

button = tk.Button(root, text="Submit", command=select_file)
button.pack()

root.mainloop()
