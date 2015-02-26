import h5py
from copy import deepcopy

# Let's load the file
file = 'data_p-unit.h5'
full_data = h5py.File(file, 'a')

# First we extract the data
data = full_data['data/p-unit']
data_arrays = data['data_arrays']
 
# We extract the responses and stimulus
responses_strong_1 = data_arrays['responses_strong/data']
responses_weak_1 = data_arrays['responses_weak/data']

stimulus_strong_1 = data_arrays['stimulus_strong/data']
stimulus_weak_1 = data_arrays['stimulus_weak/data']

# We make deep copies
responses_strong = deepcopy(responses_strong_1[:])
responses_weak = deepcopy(responses_weak_1[:])
stimulus_strong = deepcopy(stimulus_strong_1[:])
stimulus_weak = deepcopy(stimulus_weak_1[:])
