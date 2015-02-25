import numpy as np
from load_dataset import joe097 as monkey
import matplotlib.pyplot as plt


sampling_rate = 1.0  # ms
offset = -1000  # ms

data_arrays = monkey['data_arrays']
sources = monkey['sources']
tags = monkey['tags']

# Here we load the spikes activities
spike_activity_1 = data_arrays['SpikeActivity Unit 5 Target 1/data']
spike_activity_2 = data_arrays['SpikeActivity Unit 5 Target 2/data']
spike_activity_3 = data_arrays['SpikeActivity Unit 5 Target 3/data']
spike_activity_4 = data_arrays['SpikeActivity Unit 5 Target 4/data']
spike_activity_5 = data_arrays['SpikeActivity Unit 5 Target 5/data']
spike_activity_6 = data_arrays['SpikeActivity Unit 5 Target 6/data']

# Now we will build the raster plot for one of the targets

spike_activities = [spike_activity_1, spike_activity_2, spike_activity_3,
                    spike_activity_4, spike_activity_5, spike_activity_6]


mean = np.zeros(6)
time_window = 230
variability = np.array([])

for index, spike_activity in enumerate(spike_activities):
    target = index + 1
    n_trials = spike_activity.shape[1]

    time_window_spikes = spike_activity[1000:1000 + time_window]
    firing_rate = np.sum(time_window_spikes, axis=0) * 1000.0 / time_window
    ones = np.ones(firing_rate.size) * target
    plt.plot(ones, firing_rate, 'ob')
    plt.hold(True)
    mean[index] = np.mean(firing_rate)
    variability = np.concatenate((variability, firing_rate - mean[index]))

signal_variance = np.var(mean)
noise_variance = np.var(variability)
SNR = signal_variance / noise_variance

targets = np.arange(1, 7)
plt.plot(targets, mean, '-', label='SNR = ' + '{:.2f}'.format(SNR))
plt.legend()
plt.xlim([0, 7])
plt.show()
