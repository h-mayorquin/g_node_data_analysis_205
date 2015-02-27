from scipy.io import loadmat


def return_data_set(number):
    """
    Returns the actual
    """

    file_root = './data_fabian/task03_'
    extension = '.mat'
    file_core = "{:02}".format(number)
    file_address = file_root + file_core + extension
    print file_address

    data = loadmat(file_address)
    bayes_err = data['bayes_err']
    Yval = data['Yval'][:, 0]
    Xval = data['Xval']
    X = data['X']
    Y = data['Y'][:, 0]

    return X, Y, Xval, Yval, bayes_err
