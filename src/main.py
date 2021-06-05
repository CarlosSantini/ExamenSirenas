import pandas as pd
from src import config
from feature_processing import feature_process


if __name__ == '__main__':
    # Leer los archivos csv originales
    sirenas_historico = pd.read_csv(config.SIRENAS_HISTORICO)
    sirenas = pd.read_csv(config.SIRENAS)

    # Transformacion debida para los datasets
    X_train, y_train, X_test = feature_process(sirenas_historico, sirenas)



