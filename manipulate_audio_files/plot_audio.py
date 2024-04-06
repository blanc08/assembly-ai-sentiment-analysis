import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("patrick.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()

print(n_samples)

t_audio = n_samples / sample_freq

signal_array = np.frombuffer(signal_wave, dtype=np.int32)

times = np.linspace(0, t_audio, num=n_samples)

print('signal_array', signal_array)
print('times', type(times[0]))

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio signal")
plt.ylabel("Signal wave")
plt.xlabel("Time in seconds")
plt.xlim(0, t_audio)
plt.show()
