from scipy.io import loadmat

# Depression data
file_address = './data_fabian/task01.mat'
data = loadmat(file_address)
header = data['__header__']
globals = data['__globals__']
X = data['X']
Y = data['Y'][:, 0]
Xtest = data['Xtest']
