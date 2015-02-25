import numpy as np
from load_dataset import joe097 as monkey
import matplotlib.pyplot as plt
from copy import deepcopy

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

plot_raster = False
plot_hist = True

bin_size = 100.0
N_bins = int(2000.0 / bin_size)

print 'N bins =', N_bins

for target, spike_activity in enumerate(spike_activities):
    aux = spike_activity.shape[1] * bin_size
    plt.subplot(1, 6, target + 1)
    t, trial = np.nonzero(spike_activity)
    # We transform t (which is indexes) to time
    t = deepcopy(t / sampling_rate)
    t = t + offset

    # We do the rastser plot
    if plot_raster:
        plt.plot(t, trial, '*')
        plt.xlabel('Time')
        plt.ylabel('Spikes')
        plt.ylim([-1, 17])
        plt.show()

    if plot_hist:
        hist = 0
        hist, bins = np.histogram(t, bins=N_bins)
        hist = hist * 1000.0 / aux
        width = 0.7 * (bins[1] - bins[0])
        center = (bins[:-1] + bins[1:]) / 2
        plt.bar(center, hist, align='center', width=width)


plt.show()

