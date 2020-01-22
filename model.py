# NOTE: I really hate using a global variable here, but I'm not the only one that reached this conclusion. See this issue in the official rq repo https://github.com/rq/rq/issues/1088

# Preload libraries
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

def to_target_names(target):
    """This function only changes the output labels to their names"""
    if isinstance(target, np.ndarray):
        iris = load_iris()
        if len(target) == 1:
            return iris.target_names[target[0]]
        else:
            return iris.target_names[target]
    else:
        return None

def get_data():
    """Get the data. It is used in both master and worker, so better be consistent."""
    iris = load_iris()
    return train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)

def train():
    """Train the model and store it in a global variable"""
    global __model
    X_train, X_test, y_train, y_test = get_data()
    __model = RandomForestClassifier(n_jobs=2, n_estimators=20)
    __model.fit(X_train, y_train)

def predict(X_predict):
    """Predicts using the model stored in a global variable"""
    if '__model' in globals():
        return __model.predict(X_predict)
    else:
        return None