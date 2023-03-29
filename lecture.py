import pandas as pd
import matplotlib.pyplot as plt


def plot_csv(path):
    data = pd.read_csv(path, index_col="Bal", delimiter=";")
    columns = data.columns
    data_to_plot = columns[2]
    # print(data[data_to_plot])
    plt.plot(data[data_to_plot])
    plt.xlabel("Balayage")
    plt.ylabel(data_to_plot)
    plt.grid()
    plt.show()


plot_csv("debit.csv")
