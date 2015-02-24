from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# Depression data
data = loadmat('Data_depressing.mat')
V_traces = data['V_depressing']

# This has a lot of traces

V_mean = np.mean(V_traces, axis=0)


# Now we plot
plot = False
if plot:
        plt.subplot(2, 1, 1)
        plt.plot(V_mean)

        plt.subplot(2, 1, 2)
        for V in V_traces:
                plt.plot(V)

        plt.show()
