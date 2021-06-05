from sklearn import preprocessing
import pandas as pd
from src import config


def feature_process(sirenas_historico, sirenas):
    print(sirenas_historico.head())

    # Obtenemos el dataset para entrenamiento y prueba
    y_train = [x for x in sirenas_historico['especie']] # Solo tomamos los labels para transformalos
    X_test = sirenas[['v1', 'v2', 'v3', 'v4']]

    # Transformamos los labels de sirenas_historico de categorico a numerico para poder operarlo con scikit-learn
    y_train_transform = preprocessing.LabelEncoder().fit_transform(y_train)

    # Guardamos sirenas_historico.csv en un nuevo archivo llamado sirenas_historico_transformed_labels.csv para manipular con
    # mayor facilidad este dataset a futuro para la fase de entrenamiento
    df = sirenas_historico.copy()
    df['especie'] = y_train_transform
    df.to_csv(config.SIRENAS_TRANSFORMADO, index=False)

    # Leemos el archivo csv que contiene los valores de cada sirena con su respectivo label numerico
    sirenas_transform_y = pd.read_csv(config.SIRENAS_TRANSFORMADO)

    # Obtenemos los valores de cada sirena, y su etiqueta.
    X_train, y_train_t = sirenas_transform_y[['v1', 'v2', 'v3', 'v4']], [x for x in sirenas_transform_y['especie']]

    return X_train, y_train_t, X_test


