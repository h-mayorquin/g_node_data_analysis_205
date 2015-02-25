import numpy as np
from load_data_depression import V_mean
from scipy.optimize import curve_fit

last_max = 4020
x_data = np.arange(4020, V_mean.size)


def function(x, B, tau_in, tau_mem):
    aux = B * tau_in / (tau_in - tau_mem)
    return aux * (np.exp(-x / tau_in) - np.exp(-x / tau_mem))

V_data = V_mean[4020:]
p = [1.0, 1.8, 32]
parameters, covariance = curve_fit(function, x_data, V_data, p0=p)
