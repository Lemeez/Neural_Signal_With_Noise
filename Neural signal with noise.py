import numpy as np
import matplotlib.pyplot as plt

# Generate clean neural signal
time = np.linspace(0, 10, 100)
signal = np.sin(time)

# Generate random noise
noise = np.random.normal(0, 0.3, 100)

# Combine signal and noise
noisy_signal = signal + noise

plt.plot(signal, label="Clean Signal")
plt.plot(noisy_signal, label="Noisy Signal")
plt.legend()
plt.title("Neural Signal with Noise")
plt.show()