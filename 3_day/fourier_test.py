import numpy as np
import matplotlib.pyplot as plt

"""
The smallest frequency that can be represented is equal to
sample_rate / N_to_use. The bigger one is equal to half
the sampling rate
"""

sample_rate = 2.0  # Hz
step = 1 / sample_rate
t = np.arange(0, 10000, step=step)
N_data = t.size
N_to_use = 1024 * 1

print 'Smallest frequency', sample_rate / N_to_use
print 'Nyquist frequency', sample_rate / 2

f1 = 0.1  # Hz
f2 = 0.3  # Hz
f3 = 1.0  # Hz
y1 = np.sin(2 * np.pi * f1 * t)
y2 = np.sin(2 * np.pi * f2 * t)
y3 = np.sin(2 * np.pi * f3 * t)
y = y1 + y2 + y3

transform = np.fft.rfft(y, N_to_use)
# d has to be the inverse of the sample rate
freq = np.fft.fftfreq(N_to_use, d=step)
freq_aux = freq[0:N_to_use / 2]

plt.plot(freq_aux, transform[:-1], 'o-')
plt.show()
