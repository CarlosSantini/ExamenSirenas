import os


SIRENAS_HISTORICO = os.path.join(os.path.abspath(os.getcwd()),"data\sirenas_endemicas_y_sirenas_migrantes_historico.csv")
SIRENAS = os.path.join(os.path.abspath(os.getcwd()), "data\sirenas_endemicas_y_sirenas_migrantes.csv")
SIRENAS_TRANSFORMADO = os.path.join(os.path.abspath(os.getcwd()), "data\sirenas_historico_transformed_labels.csv")

# Seleccion de algoritmo
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
MODELO = 'NearestCentroid'

# SIRENAS_HISTORICO = '../data/sirenas_endemicas_y_sirenas_migrantes_historico.csv'
# SIRENAS = '../data/sirenas_endemicas_y_sirenas_migrantes.csv'
# SIRENAS_TRANSFORMADO = '../data/sirenas_historico_transformed_labels.csv'

# def dict_variables():
#     SIRENAS_HISTORICO = '../data/sirenas_endemicas_y_sirenas_migrantes_historico.csv'
#     SIRENAS = '../data/sirenas_endemicas_y_sirenas_migrantes.csv'
#     SIRENAS_TRANSFORMADO = '../data/sirenas_historico_transformed_labels.csv'
#
#     # Seleccion de algoritmo
#     '''
#         "NearestCentroid"
#         "MLPClassifier"
#         "SGDClassifier"
#         "LogisticRegression"
#         "SVC1"
#         "SVC2"
#         "DecisionTree"
#         "RandomForest"
#     '''
#     MODELO = 'NearestCentroid'
#
#     dicc = {'SIRENAS_HISTORICO':SIRENAS_HISTORICO,
#             'SIRENAS':SIRENAS,
#             'SIRENAS_TRANSFORMADO':SIRENAS_TRANSFORMADO,
#             'MODELO': MODELO}
#
#     return dicc
