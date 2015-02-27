from sklearn.linear_model import LogisticRegression
from sklearn.grid_search import GridSearchCV
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

    return rsearch.best_estimator_, rsearch.best_score_, rsearch
