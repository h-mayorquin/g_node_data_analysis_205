import numpy as np
from load_data import X, Y, Xtest
from sklearn.linear_model import LogisticRegression
from sklearn.grid_search import GridSearchCV
from scipy.io import savemat
from sklearn.cross_validation import StratifiedKFold


def return_best_model(X, Y, N, C, penalties):
    """
    Returns the best model for X data and Y targets
    """
    skf = StratifiedKFold(Y, N)

    # We define the logistic regression
    lg = LogisticRegression()

    param_grid = [{'C': C, 'penalty': penalties}]

    rsearch = GridSearchCV(estimator=lg, param_grid=param_grid, cv=skf)
    rsearch.fit(X, Y)
g    
    return rsearch.best_estimator_, rsearch.best_score_, rsearch


Y = Y.astype('int')
C = np.arange(0.05, 2, 0.05)
C = C.tolist()
penalties = ['l1', 'l2']
N = 4

skf = StratifiedKFold(Y, N)


# We define the logistic regression
lg = LogisticRegression()

param_grid = [{'C': C, 'penalty': penalties}]


x, y, rsearch = return_best_model(X, Y, 3, C, penalties)
print y
Ydata = rsearch.predict(Xtest)
dict_to_save = {'Y': Ydata}
file = 'ramon_labels.mat'
savemat(file, dict_to_save)
