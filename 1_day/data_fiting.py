import numpy as np
import matplotlib.pyplot as plt
from load_data_depression import V_mean
from scipy.signal import argrelextrema


T_data = 1200
dt_data = 1000.0 / 4000
times_data = np.arange(0, T_data, dt_data)

if True:
    plt.plot(V_mean, label='V_experiment')
    plt.legend()
    plt.ylim([-0.5, 3])
    #plt.xlim([-100, T_data])
    plt.hold(True)

# We need to extract a vector of the maximums
arg_maximums = argrelextrema(V_mean, np.greater, order=100)[0]
arg_minium = argrelextrema(V_mean, np.less, order=100)[0]
tol = 0.5
tol_min = 1e-8

# From all the maximus we extract those ones that are
arg_maximums_true = []
for arg in arg_maximums:
    if V_mean[arg] > tol:
        arg_maximums_true.append(arg)
        

arg_minium_true = []
for arg in arg_minium:
    if (V_mean[arg] - V_mean[0]) > tol_min:
        arg_minium_true.append(arg)


arg_minium_true.append(arg_minium[-2])
arg_minium_true.append(arg_minium[1])

values_min = V_mean[arg_minium_true]
values_max = V_mean[arg_maximums_true]
plt.plot(arg_maximums_true, values_max, 'or', markersize=10)
plt.hold(True)
plt.plot(arg_minium_true, V_mean[arg_minium_true], 'og', markersize=10)
plt.show()


Amp_data = V_mean[arg_maximums_true] - V_mean[arg_minium_true]



