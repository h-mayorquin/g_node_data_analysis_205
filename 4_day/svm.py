import numpy as np
from load_data import X, Y, Xtest
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import train_test_split


def return_best_svm(X, Y, N, C, penalties):
    """
    Returns the best model for X data and Y targets
    """
    skf = StratifiedKFold(Y, N)

    # We define the logistic regression
    lg = SVC(tol=0.0001)

    param_grid = [{'C': C, 'kernel': penalties}]

    rsearch = GridSearchCV(estimator=lg, param_grid=param_grid, cv=skf)
    rsearch.fit(X, Y)
    
    return rsearch.best_estimator_, rsearch.best_score_, rsearch


C = np.arange(0.05, 2, 0.05)
C = C.tolist()
penalties = ['poly', 'rbf', 'sigmoid']
N = 5

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10)

for N in range(2, 10):
    model, score, rsearch = return_best_svm(X_train,
                                            Y_train, N, C, penalties)
    print '--------------'
    print 'Foldls', N
    print 'Score', score
    print 'generalization', rsearch.score(X_test, Y_test)



