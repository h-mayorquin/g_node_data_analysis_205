import numpy as np
import matplotlib.pyplot as plt
from math import exp

size = 9
dt = 50.0  # ms
dt_2 = 550.0

# Vectors to fit
x_fit = np.zeros(size)
V_max_fit = np.zeros(size)
V0_fit = np.zeros(size)

# Paramters of the model
tau_rec = 1000.0  # ms
tau_mem = 32.0  # ms
tau_in = 1.8  # ms
A = 144.0
u = 0.26

# First we will fit x

x_fit[0] = 1

for i in range(size - 2):
    x_fit[i+1] = x_fit[i] * (1 - u) * exp(-dt / tau_rec)
    + 1 - exp(-dt / tau_rec)

# Last value of x_fit


x_fit[-1] = x_fit[-2] * (1 - u) * exp(-dt_2 / tau_rec)
+ 1 - exp(-dt_2 / tau_rec)

# We calculate alpha fit
alpha_fit = u * A * x_fit

# Now we calculate V_0 and V_max
V0_fit[0] = 0

tau_diff = tau_in - tau_mem

for k in range(size - 1):
    ex1 = exp(-dt / tau_in)
    ex2 = exp(-dt / tau_mem)
    print 'ex1 ex2', ex1, ex2
    problem = ex1 - ex2
    print 'problem', problem
    this = alpha_fit[k] * tau_in / tau_diff
    print 'this', this
    that = V0_fit[k] * exp(-dt / tau_mem)
    print 'that', that
    V0_fit[k + 1] = that + this * problem

for k in range(size - 1):
    aux2 = (alpha_fit[k] * tau_in - V0_fit[k] * tau_diff)
    #print 'aux', aux2
    aux = alpha_fit[i] * tau_mem / aux2
    V_max_fit[k] = alpha_fit[k] * (aux ** (tau_mem / tau_diff))

# The final values
ex1 = np.exp(-dt_2 / tau_in)
ex2 = np.exp(-dt_2 / tau_mem)
print 'ex1 ex2', ex1, ex2
problem = ex1 - ex2 
problem = ex1 - ex2
this = alpha_fit[-2] * tau_in / tau_diff
that = V0_fit[-2] * exp(-dt_2 / tau_mem)
V0_fit[-1] = that + this * problem

aux = alpha_fit[-1] * tau_mem / (alpha_fit[-1]
                                 * tau_in - V0_fit[-1] * tau_diff)

V_max_fit[-1] = alpha_fit[-1] * (aux ** (tau_mem / tau_diff))


amp_fit = V_max_fit - V0_fit

# Finally we plot
plt.subplot(1, 2, 1)
plt.plot(x_fit, '*-', label='x_fit')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(V_max_fit, '*-', label='Vmax_fit')
plt.hold(True)
plt.plot(V0_fit, '*-', label='V0_fit')
plt.legend()
plt.show()

