import numpy as np
import matplotlib.pyplot as plt
from load_data import responses_strong, stimulus_strong


# General values of the data
sampling_rate = 20000.0  # Hz
N_data = stimulus_strong.size
N_trials = responses_strong.shape[1]

# First we extract the spikes
spike_indexes, trial = np.nonzero(responses_strong)

window = 1000  # This is equivalent to 50 ms
st = np.zeros((spike_indexes.size, window))

spike_indexes = spike_indexes[spike_indexes > window]

for index, spike_index in enumerate(spike_indexes):
    st[index] = stimulus_strong[spike_index - window: spike_index]


time = np.arange(window)
time = time * 1000.0 / sampling_rate  # Puts time in milliseconds
sta = np.mean(st, axis=0)
plt.plot(- time[::-1], sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.show()


