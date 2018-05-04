#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#read audio file
# sampling_freq, signal = wavfile.read('wav/random_sound.wav')

sampling_freq, signal = wavfile.read('data/stop/0c40e715_nohash_0.wav')

#display params
print('\nSignal shape:', signal.shape)
print('Datatype:',signal.dtype)
print('Signal duration:', round(signal.shape[0] / float(sampling_freq), 2), 'seconds')

#normalize the signal
signal = signal/np.power(2,15)

#extract first 50 values
# signal = signal[:500]

#construct the time axis in milliseconds
time_axis = 1000 * np.arange(0, len(signal),1)/float(sampling_freq)

#plot audio signal
plt.plot(time_axis,signal, color="black")
plt.xlabel('Time (milliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')
plt.show()