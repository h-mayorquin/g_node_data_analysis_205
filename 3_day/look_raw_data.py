import numpy as np
import matplotlib.pyplot as plt
from load_data import responses_strong, stimulus_strong

sampling_rate = 20000.0  # Hz
N_data = stimulus_strong.size
N_trials = responses_strong.shape[1]

bin_size = 200.0  # ms
N_bins = int(N_data / bin_size)

window_to_plot = range(0, N_data / 10)


t, trial = np.nonzero(responses_strong[window_to_plot, :])

# Let's transform the time vector
t = t / sampling_rate
time = np.arange(stimulus_strong.size)
time = time / sampling_rate

plt.subplot(1, 2, 1)
plt.plot(time[window_to_plot], stimulus_strong[window_to_plot])
plt.xlabel('Time (s)')
plt.ylabel('Stimulus intensity')


plt.subplot(1, 2, 2)
plt.plot(t, trial, '*')
plt.xlabel('Time (s)')
plt.ylabel('Spikes')
plt.ylim([-1, N_trials + 1])
plt.show()

hist = 0
hist, bins = np.histogram(t, bins=N_bins)
hist = hist * 1000.0 / (N_trials * bin_size)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()

