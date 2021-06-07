from sklearn import preprocessing
import pandas as pd
from src.config import SIRENAS_TRANSFORMADO
import matplotlib.pyplot as plt
import os


def plot_scatters(migrante, endemica, carac_x, carac_y):
    ruta = os.path.join(os.path.abspath(os.getcwd()), "plots")

    plot_migrante = plt.scatter(migrante[carac_x], migrante[carac_y], color='r')
    plot_endemica = plt.scatter(endemica[carac_x], endemica[carac_y], color='b')

    plt.xlabel(carac_x, fontsize=15)
    plt.ylabel(carac_y, fontsize=15)
    plt.legend([plot_migrante, plot_endemica], ['migrante', 'endemica'])
    plt.title(carac_x + " vs " + carac_y + ".png")
    plt.savefig(ruta + "\scatter_" + carac_x + "_vs_" + carac_y + ".png")
    # plt.show()


def feature_process(sirenas_historico, sirenas):
    # print(sirenas_historico.head())

    # Obtenemos el dataset para entrenamiento y prueba
    X_train, y_train = sirenas_historico[['v1', 'v2', 'v3', 'v4']], sirenas_historico[
        'especie']  # Solo tomamos los labels para transformalos
    X_test = sirenas[['v1', 'v2', 'v3', 'v4']]

    # scatter plots entre cada par de caracteristicas de sirenas historicas
    migrante = sirenas_historico[sirenas_historico['especie'] == 'sirena_migrante']
    endemica = sirenas_historico[sirenas_historico['especie'] == 'sirena_endemica']
    plot_scatters(migrante, endemica, 'v1', 'v2')
    plot_scatters(migrante, endemica, 'v1', 'v3')
    plot_scatters(migrante, endemica, 'v1', 'v4')
    plot_scatters(migrante, endemica, 'v2', 'v3')
    plot_scatters(migrante, endemica, 'v2', 'v4')
    plot_scatters(migrante, endemica, 'v3', 'v4')

    # Transformamos los labels de sirenas_historico de categorico a numerico para poder operarlo con scikit-learn
    le = preprocessing.LabelEncoder()
    y_train_transform = le.fit_transform(y_train)

    # Guardamos sirenas_historico.csv en un nuevo archivo llamado sirenas_historico_transformed_labels.csv para manipular con
    # mayor facilidad este dataset a futuro para la fase de entrenamiento
    df = sirenas_historico.copy()
    df['especie'] = y_train_transform
    df.to_csv(SIRENAS_TRANSFORMADO, index=False)

    # Leemos el archivo csv que contiene los valores de cada sirena con su respectivo label numerico
    sirenas_transform_y = pd.read_csv(SIRENAS_TRANSFORMADO)

    # Obtenemos los valores de cada sirena, y su etiqueta.
    X_train, y_train_t = sirenas_transform_y[['v1', 'v2', 'v3', 'v4']], [x for x in sirenas_transform_y['especie']]

    return X_train, y_train_t, X_test, le
