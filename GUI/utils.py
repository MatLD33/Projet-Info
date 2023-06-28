import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def str_to_float(number):
    num = number.split(",")
    if len(num) == 1:
        return float(num[0])
    else:
        return float(num[0] + "." + num[1])


str_to_float_v = np.vectorize(str_to_float)


def time_to_float(ts):
    return sum(float(x) * 60**i for i, x in enumerate(reversed(ts.split(":"))))


time_to_float_v = np.vectorize(
    time_to_float
)  # Vectorisation de la fonction time_to_float


def new_name(path, ext):
    componants = path.split("\\")
    name = componants[-1]
    name2 = name[:-4]
    return name2 + "." + ext


def create_data(path, n, data_type="value"):
    """
    Cette fonction retourne les données d'un fichier csv
    Elle retroune les données de la colonne n

    x : abscisses en numéro de balayage
    data_to_plot : nom de la donnée
    val : valeur des données en float ou time
    """
    data = pd.read_csv(path, index_col="Bal", delimiter=";")
    columns = data.columns
    data_to_plot = columns[n]
    if data_type == "value":
        val = str_to_float_v(data[data_to_plot].values)
    elif data_type == "time":
        val = time_to_float_v(data[data_to_plot].values)
    x = np.arange(0, len(val))
    return x, data_to_plot, val


def plot_csv(path, n):
    """
    Cette fonction permet de tracer les données d'un fichier csv présent en colonne n
    """
    x, data_to_plot, val = create_data(path, n)  # Récupération des données

    plt.figure()
    plt.plot(val)
    plt.xlabel("Balayage")
    plt.ylabel(data_to_plot)
    plt.grid()
    plt.savefig("Plot\\" + new_name(path, "png"))
    plt.show()


def detect_stable_stage(path, precision=0.1, window_size=100, plot=False):
    """
    Cette fonction permet de détecter les paliers stables d'un fichier csv
    Elle retourne une matrice de taille (nb_stages,4) avec :
    - La première colonne : le début du palier (en numéro de balayage)
    - La deuxième colonne : la fin du palier (en numéro de balayage)
    - La troisième colonne : le début du palier (en temps)
    - La quatrième colonne : la fin du palier (en temps)
    - La cinquième colonne : la moyenne du palier
    - La sixième colonne : la variance du palier

    path : chemin du fichier csv
    precision : seuil de la variance pour détecter un palier
    window_size : taille de la fenêtre de calcul de la variance
    plot : booléen pour afficher le graphe de la variance
    """
    x, data_to_plot, values = create_data(path, 2)  # Récupération des données
    x, data_to_plot, times = create_data(
        path, 1, data_type="time"
    )  # Récupération des données

    n = len(values)
    variances = np.empty(n - window_size)  # tableau des variances
    means = np.empty(n - window_size)  # tableau des moyennes

    for i in range(n - window_size):
        window_data = values[i : i + window_size]  # fenêtre de données
        var = np.var(window_data)
        mean = np.mean(window_data)
        variances[i] = var
        means[i] = mean

    points_stage = np.where(variances < precision)[0]
    points_stage_by_stage = np.split(
        points_stage, np.where(np.diff(points_stage) != 1)[0] + 1
    )  # séparation des paliers
    nb_stages = len(points_stage_by_stage)  # nombre de paliers

    stages_matrix = np.empty((nb_stages, 6))  # matrice des paliers
    stages_matrix[:, 0] = list(map(min, points_stage_by_stage))
    stages_matrix[:, 1] = list(map(max, points_stage_by_stage))
    stages_matrix[:, 2] = times[stages_matrix[:, 0].astype(int)]
    stages_matrix[:, 3] = times[stages_matrix[:, 1].astype(int)]
    stages_matrix[:, 4] = means[stages_matrix[:, 0].astype(int)]
    stages_matrix[:, 5] = variances[stages_matrix[:, 0].astype(int)]

    if plot:
        plt.plot(variances)
        plt.plot([precision] * (n - window_size), "r")
        plt.ylabel("Variance")
    return stages_matrix


def stables_stage_plot(path, precision=0.1, window_size=100):
    """
    Cette fonction permet de tracer les paliers stables d'un fichier csv
    """
    x, data_to_plot, values = create_data(path, 2)  # Récupération des données
    x, time_to_plot, times = create_data(
        path, 1, data_type="time"
    )  # Récupération des données

    stages_matrix = detect_stable_stage(
        path, precision, window_size
    )  # Récupération des données

    plt.figure()
    plt.plot(values)
    plt.xlabel("Balayage")
    plt.ylabel(data_to_plot)
    for (start, end, start_time, end_time, mean, var) in stages_matrix:
        plt.plot(x[int(start) : int(end)], mean * np.ones(int(end) - int(start)), "r")
        plt.grid()

    plt.show()


def stables_stage_csv(path, precision=0.1, window_size=100):
    """
    Cette fonction permet de retourne les paliers stables d'un fichier csv
    Elle retourne une dataframe de taille (nb_stages,4) avec :
    - La première colonne : le début du palier
    - La deuxième colonne : la fin du palier
    - La troisième colonne : le début du palier (en temps)
    - La quatrième colonne : la fin du palier (en temps)
    - La cinquièle colonne : la moyenne du palier
    - La sixième colonne : la variance du palier
    """
    stages_matrix = detect_stable_stage(path, precision, window_size)
    nb_stages = len(stages_matrix)
    ind = np.arange(nb_stages)
    df = pd.DataFrame(
        stages_matrix,
        index=ind,
        columns=[
            "Debut (Bal)",
            "Fin (Bal)",
            "Debut (Temps)",
            "Fin (Temps)",
            "Moyenne",
            "Variance",
        ],
    )
    df.to_csv("Plot\\mat_" + new_name(path, "csv"))
    return df


def polynomial_interpolation(x, y, degree):
    """
    Cette fonction permet de faire une interpolation polynomiale
    Elle retourne le polynome d'interpolation
    """
    poly = np.polynomial.polynomial.Polynomial.fit(x, y, degree)
    return poly


def linear_interpolation(x, y):
    """
    Cette fonction effectue une interpolation linéaire entre les données x et y
    """
    coeffs = np.polyfit(x, y, 1)
    return np.poly1d(coeffs)


def comparaison_sondes(n1, n2, graph=True):
    """
    Cette fonction permet de comparer les sondes n1 et n2
    Elle retourne un graphe de comparaison si nécessaire
    """
    x, name, y1 = create_data("Data\Sondes.csv", n1)
    x, name, y2 = create_data("Data\Sondes.csv", n2)
    p = linear_interpolation(y1, y2)
    z = p(y1)
    if graph:
        plt.figure()
        plt.plot(y1, y2)
        plt.plot(y1, z)
        plt.grid()
        plt.show()
    return p
