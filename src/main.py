import pandas as pd
from src import config
from feature_processing import feature_process
from train import training


def save_sirenas_migrantes(file, y_predicts, le):
    # print(file.columns)
     # funcion para convertir las etiquetas de 0,1 a "endemica" o "migrante"
    y_predicts = le.inverse_transform(y_predicts)

    # actualiza la etiqueta correspondiente dentro del archivo "sirenas_endemicas_y_sirenas_migrantes.csv"
    file['especie'] = y_predicts
    file.to_csv(config.SIRENAS, index=False)


if __name__ == '__main__':
    # Leer los archivos csv originales
    sirenas_historico = pd.read_csv(config.SIRENAS_HISTORICO)
    sirenas = pd.read_csv(config.SIRENAS)

    # Transformacion debida para los datasets
    X_train, y_train, X_test, le = feature_process(sirenas_historico, sirenas)

    '''
    "NearestCentroid"
    "MLPClassifier"
    "SGDClassifier"
    "LogisticRegression"
    "SVC1"
    "SVC2"
    "DecisionTree"
    "RandomForest"
    '''

    y_test = training(X_train, y_train, X_test, 'NearestCentroid')

    save_sirenas_migrantes(sirenas, y_test, le)
