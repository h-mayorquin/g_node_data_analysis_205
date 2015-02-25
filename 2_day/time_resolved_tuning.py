import numpy as np
from load_dataset import joe097 as monkey
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy
from math import floor

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


spike_activities = [spike_activity_1, spike_activity_2, spike_activity_3,
                    spike_activity_4, spike_activity_5, spike_activity_6]


window_size = 200
w = floor(window_size * sampling_rate)
boxcar = scipy.signal.get_window('hamming', w)

for activity_index, activity in enumerate(spike_activities):
    
    plt.subplot(3, 2, activity_index + 1)
    N_trials = activity.shape[1]
    N_points = activity.shape[0]
    total_data = np.zeros((N_trials, N_points))
    data = np.array(activity)
    
    for index, signal in enumerate(data.T):

        # Convolution
        conv = np.convolve(signal, boxcar, 'same')
        # Transform to Hz
        conv = 1000.0 * conv / window_size
        # Store for later calculation of the mean
        total_data[index] = conv

        plt.plot(conv, color='0.55')
        plt.hold(True)

    mean = np.mean(total_data, axis=0)
    plt.plot(mean,  color='k', linewidth=5.0, label='mean of trials')
    plt.xlabel('Time (ms)')
    plt.ylabel('Firing rate (Hz)')
    #red_patch = mpatches.Patch(color='red', label='The red data')
    #plt.legend(handles=[red_patch])
    # Trying
    plt.legend()


plt.show()

