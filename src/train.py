from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import NearestCentroid
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


def plot_confusion_matrix(cm, title='Matriz de Confusion', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


def training(X_train, y_train, X_test, modelo):
    MODELS = {
        "NearestCentroid": NearestCentroid(),
        "MLPClassifier": MLPClassifier(),
        "SGDClassifier": SGDClassifier(),
        "LogisticRegression": LogisticRegression(),
        "SVC1": SVC(kernel="linear", C=0.025),
        "SVC2": SVC(gamma=2, C=1),
        "DecisionTree": DecisionTreeClassifier(max_depth=5),
        "RandomForest": RandomForestClassifier(max_depth=None, n_estimators=10, max_features=1)
    }

    model = MODELS[modelo]

    model.fit(X_train, y_train)
    # y_predict = model.predict(X_train)
    # print("Predicciones con dataset de entrenamiento:\n"+y_predict)
    # cm = confusion_matrix(y_train_t, y_predicted)
    # plot_confusion_matrix(cm)
    # print(accuracy_score(y_train, y_predict))

    y_predict = model.predict(X_test)
    # print("Predicciones con dataset de prueba:\n" , y_predict)

    return y_predict
