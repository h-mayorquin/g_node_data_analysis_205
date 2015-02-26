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
kernel = scipy.signal.get_window(('gaussian', 100), w)
kernel2 = scipy.signal.get_window(('gaussian', 50), w)
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

if plot_firing_rate:
    plt.plot(time, firing_rate,  color='k',
             linewidth=5.0, label='mean of trials')
    plt.xlabel('Time (ms)')
    plt.ylabel('Firing rate (Hz)')
    plt.show()


# We normalize to calculate the correlations
stimulus_strong -= np.mean(stimulus_strong)
stimulus_strong /= np.std(stimulus_strong) * len(stimulus_strong)

firing_rate -= np.mean(firing_rate)
firing_rate /= np.std(firing_rate)

# Now we calculate the correlation
xcorr = np.correlate(stimulus_strong, firing_rate, mode=mode)

correlation_window = size_to_use * 1000.0 / (sampling_rate * 2)

correlation_time = time - correlation_window
if plot_correlation:
    plt.plot(correlation_time, xcorr)
    plt.xlabel('Time (ms)')
    plt.ylabel('Correlation normalized')
    plt.xlim([-correlation_window, correlation_window])
    plt.show()


    
