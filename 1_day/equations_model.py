import numpy as np
import matplotlib.pyplot as plt
from load_data_depression import V_mean

# First the parameters of the model
tau_rec = 1000  # ms
tau_mem = 32  # ms
tau_in = 1.8  # ms
A = 144
u = 0.26

#u = 1.0

# Then the paramters of the simulation
dt = 0.1  # ms
T = 1200  # ms
Nt = int(T / dt)  # Total time of the simulation

x = np.zeros(Nt)
y = np.zeros(Nt)
V = np.zeros(Nt)

# Then the input
freq = 20.0  # Hz
freq = 20.0 / 1000  # Transform to MHz
spike_time = 1.0 / freq
spikes = []  # List with spikes

# First let's put the systematic spikes in ms
for i in range(8):
    spikes.append(spike_time * i)

spikes.append(spikes[-1] + 550)  # We add the lonley spikes

# Transform the spikes into a vector
spike_vector = np.zeros(Nt)
for spike in spikes:
    spike_to_index = int(spike * 1.0 / dt)
    print 'spike', spike
    print 'spike_index', spike_to_index
    spike_vector[spike_to_index] = 1


# Initial conditions
x[0] = 1
y[0] = 0
V[0] = 0

spike_dummy = 1

# Then the simulation
for t in range(Nt - 1):
    x[t + 1] = (((1 - x[t]) / tau_rec) - u * x[t] * spike_vector[t] / dt) * dt + x[t]
    y[t + 1] = (-y[t] / tau_in + u * x[t] * spike_vector[t] / dt) * dt + y[t]
    V[t + 1] = (-V[t] + A * y[t]) * (dt / tau_mem) + V[t]


# Now we plot the results

times = np.arange(0, T, dt)
times_data = np.arange(0, 1200, 0.25)

plt.subplot(1, 3, 1)
plt.plot(times, x, label='x')
plt.hold(True)
plt.plot(times, y, label='y')
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(times, V, label='V_simulated')
plt.legend()
plt.xlabel('Time (ms)')
plt.ylim([-0.5, 3])

plt.subplot(1, 3, 3)
plt.plot(times_data, V_mean, label='V_experiment')
plt.legend()
plt.ylim([-0.5, 3])
plt.show()
    
