import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from load_data import responses_strong, stimulus_strong
from math import floor

plot_firing_rate = True
plot_correlation = True

ratio = 0.1
size_to_use = int(ratio * stimulus_strong.size)
stimulus_strong = stimulus_strong[0:size_to_use]
responses_strong = responses_strong[0:size_to_use, :]

# General values of the data
sampling_rate = 20000.0  # Hz
N_data = stimulus_strong.size
N_trials = responses_strong.shape[1]
time = np.arange(0, N_data) * 1000.0 / sampling_rate  # in ms

window_size = 100.0  # ms
window_size = window_size / 1000.0  # s

w = floor(window_size * sampling_rate)
kernel = scipy.signal.get_window(('gaussian', 25), w)

firing_rates = np.zeros((N_trials, N_data))
mode = 'same'

for index, signal in enumerate(responses_strong.T):

    conv = np.convolve(signal, kernel, mode=mode) / window_size
    firing_rates[index] = conv

    if plot_firing_rate:
        plt.plot(time, conv, color='0.55')
        plt.hold(True)


firing_rate = np.mean(firing_rates, axis=0)
N_to_use = 2 ** 14
step = 1 / sampling_rate
transform = np.fft.rfft(firing_rate, N_to_use)
freq = np.fft.fftfreq(N_to_use, d=step)
freq_aux = freq[0:N_to_use / 2]

power = np.abs(transform[:-1])**2
plt.plot(freq_aux, power, 'o-')
plt.show()

# Plot the things
#plt.subplot(1, 2, 1)


#plt.subplot(1, 2, 2)
