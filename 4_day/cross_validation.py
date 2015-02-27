import numpy as np
from load_data import X, Y, Xtest
from sklearn.linear_model import LogisticRegression
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import train_test_split


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
    
    return rsearch.best_estimator_, rsearch.best_score_, rsearch

Y = Y.astype('int')

C = np.arange(0.05, 3, 0.01)
C = C.tolist()
penalties = ['l1', 'l2']
param_grid = [{'C': C, 'penalty': penalties}]
N = 10

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10)

for N in range(2, 10):
    model, score, rsearch = return_best_model(X_train,
                                              Y_train, N, C, penalties)
    print N
    print score
    print rsearch.score(X_test, Y_test)

