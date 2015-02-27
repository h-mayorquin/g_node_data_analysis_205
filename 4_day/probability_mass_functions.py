import numpy as np
from load_big_data_set import return_data_set
from model_selection import return_best_model
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def get_probabilities(number):
    """
    Returns the joint probabilities
    """
    X, Y, Xval, Yval, bayes_err = return_data_set(number)

    Y = Y.astype('int')
    C = np.arange(0.1, 2, 0.1)
    C = C.tolist()
    penalties = ['l1', 'l2']
    N = 4

    best_estimator, best_score, rsearch = return_best_model(X, Y,
                                                            N, C, penalties)
    Yval_predictions = rsearch.predict(Xval)
    Y_predictions = rsearch.predict(X)
    rights = np.sum((Yval - Yval_predictions) == 0)
    classification_acc = rights * 100.0 / len(Yval)  # Accuaracy

    Y_total = np.hstack((Y, Yval))
    Ypredction_total = np.hstack((Y_predictions, Yval_predictions))
    cm = confusion_matrix(Y_total, Ypredction_total)
    joint = cm * 1.0 / np.sum(cm)

    py_normal = np.sum(cm, axis=1) * 1.0 / np.sum(cm)
    py_predicted = np.sum(cm, axis=0) * 1.0 / np.sum(cm)

    return py_normal, py_predicted, joint, classification_acc


def calculate_MI(py_normal, py_predicted, joint):
    """
    Calculates the Mutual Information for two distributions probabilites
    """
    # Calculate entropy
    H_normal = -np.sum(py_normal * np.log2(py_normal))
    H_predicted = -np.sum(py_predicted * np.log2(py_predicted))
    H_joint = -np.sum(joint * np.log2(joint))

    MI = H_normal + H_predicted - H_joint

    return MI


# Take the data from the file
X, Y, Xval, Yval, bayes_err = return_data_set(4)
mi_to_plot = []
accuracy_to_plot = []
bayes_err = bayes_err[0, :]

for number in range(1, 26):

    py_normal, py_predicted, joint, classification_acc = get_probabilities(number)
    MI = calculate_MI(py_normal, py_predicted, joint)
    accuracy_to_plot.append(classification_acc / 100.0)
    mi_to_plot.append(MI)


plt.plot(bayes_err, accuracy_to_plot, label='accuracy')
plt.hold(True)
plt.xlabel('Optimal error')
plt.plot(bayes_err, mi_to_plot, label='MI')
plt.legend()
plt.show()
