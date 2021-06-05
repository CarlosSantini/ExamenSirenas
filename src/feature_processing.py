from sklearn import preprocessing
import pandas as pd
from src import config


def feature_process(sirenas_historico, sirenas):
    print(sirenas_historico.head())

    # Obtenemos el dataset para entrenamiento y prueba
    X_train, y_train = sirenas_historico[['v1', 'v2', 'v3', 'v4']], [x for x in sirenas_historico['especie']]
    X_test = sirenas[['v1', 'v2', 'v3', 'v4']]

    # Transformamos los labels de sirenas_historico de categorico a numerico para poder operarlo con scikit-learn
    y_train_transform = preprocessing.LabelEncoder().fit_transform(y_train)

    # Guardamos sirenas_historico.csv en un nuevo archivo llamado sirenas_historico_transformed_labels.csv para manipular con
    # mayor facilidad este dataset a futuro para la fase de entrenamiento
    df = sirenas_historico.copy()
    df['especie'] = y_train_transform
    df.to_csv(config.SIRENAS_TRANSFORMADO, index=False)



