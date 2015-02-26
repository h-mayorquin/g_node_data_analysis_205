from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# Load the data from mat file
data = loadmat('surrogateData.mat')
y = data['y'][0, :]


N_data = y.size
# can be mutiplied by then if not average
N_to_use = 2 ** 12
sampling_rate = 4096.0  # Hz
nyquist_frequency = sampling_rate / 2.0
step = 1 / sampling_rate

print 'Smallest frequency', sampling_rate / N_to_use
print 'Nyquist frequency', sampling_rate / 2

transforms = np.zeros((10, int(nyquist_frequency) + 1))
average = False


if average:

    for i in range(10):
        # Signal
        signal = y[i*N_to_use:(i+1)*N_to_use]
        # Do the fourier transform
        transforms[i] = np.fft.rfft(y, N_to_use)

    # Calculate the frequencies

    transform = np.mean(transforms, axis=0)

else:
    transform = np.fft.rfft(y, N_to_use)

freq = np.fft.fftfreq(N_to_use, d=step)
freq_aux = freq[0:N_to_use / 2]

power = np.abs(transform[:-1])**2
plt.plot(freq_aux, power, 'o-')
plt.show()


