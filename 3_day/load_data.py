import h5py
from copy import deepcopy

# Let's load the file
file = 'data_p-unit.h5'
full_data = h5py.File(file, 'a')

# First we extract the data
data = full_data['data/p-unit']
data_arrays = data['data_arrays']
 
# We extract the responses and stimulus
responses_strong = data_arrays['responses_strong/data']
responses_weak = data_arrays['responses_weak/data']

stimulus_strong = data_arrays['stimulus_strong/data']
stimulus_weak = data_arrays['stimulus_weak/data']

# We make deep copies
responses_strong = deepcopy(responses_strong)
responses_weak = deepcopy(responses_weak)
stimulus_strong = deepcopy(stimulus_strong)
stimulus_weak = deepcopy(stimulus_weak)
