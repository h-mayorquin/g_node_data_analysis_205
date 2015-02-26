import numpy as np
import matplotlib.pyplot as plt
from load_data import responses_strong, stimulus_strong

sampling_rate = 20000.0  # Hz

bin_size = 100.0
N_bins = int(2000.0 / bin_size)

window_to_plot = range(0, 10000)


t, trial = np.nonzero(responses_strong[window_to_plot, :])

# Let's transform the time vector
t /= sampling_rate
time = np.arange(stimulus_strong.size)
time /= sampling_rate

plt.subplot(1, 2, 1)
plt.plot(stimulus_strong[window_to_plot])

plt.subplot(1, 2, 2)
plt.plot(t, trial, '*')
plt.xlabel('Time')
plt.ylabel('Spikes')
plt.ylim([-1, 17])
plt.show()



