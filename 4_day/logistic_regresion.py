import numpy as np
from load_data import X, Y
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

Y = Y.astype('int')


c_set = np.arange(0.1, 1, 0.1)
error_set = np.zeros(c_set.size)
error_set_l1 = np.zeros(c_set.size)
error_set_l2 = np.zeros(c_set.size)

penalities = ['l1', 'l2']

for penality in penalities:
    for index, C in enumerate(c_set):

        # We define the logistic regression
        lg = LogisticRegression(penalty=penality, dual=False, tol=0.0001,
                                C=C, fit_intercept=True, intercept_scaling=1,
                                class_weight=None, random_state=None)

        # We fit the regresssion
        lg.fit(X, Y)
        class_error = lg.score(X, Y)
        if penality == 'l1':
            error_set_l1[index] = class_error
        if penality == 'l2':
            error_set_l2[index] = class_error

# We calculate generalization error
plt.plot(c_set, error_set_l1, label='l1')
plt.hold(True)
plt.plot(c_set, error_set_l2, label='l2')
plt.xlabel('Percentage of correctly classified data')
plt.ylabel('rsm value')
plt.legend()
plt.show()

# Plot in 3D
plot_3d = True
aux_x = np.arange(-5, 5, 0.1)
aux_y = np.arange(-5, 5, 0.1)
grid = np.meshgrid(aux_x, aux_y)
x = grid[0].ravel()
y = grid[1].ravel()
aux = np.vstack((x, y)).T
z = lg.decision_function(aux)
z = lg.predict_proba(aux)
if plot_3d:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z[:, 0], rstride=10, cstride=10)
    
    plt.show()

