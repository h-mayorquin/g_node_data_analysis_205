import h5py


# First extract the file
file = 'module2.h5'
f = h5py.File(file, 'a')

# Extract data and metadata
data = f['data']
metadata = f['metadata']

# Extract the data
joe097 = data['joe097']
joe108 = data['joe108']
joe147 = data['joe147']
joe151 = data['joe151']

data_arrays = joe097['data_arrays']
sources = joe097['sources']
tags = joe097['tags']

# Extract the metadata
General = metadata['General']
Experiment = metadata['Experiment']
Sessions = metadata['Sessions']

