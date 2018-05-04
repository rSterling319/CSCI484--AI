#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#read audio file
sampling_freq, signal = wavfile.read('wav/spoken_word.wav')

#normalize the values
signal = signal /np.power(2,15)

#extract lenght of audio signal
len_signal = len(signal)

#extract half lenght
len_half = np.ceil((len_signal +1)/2.0).astype(np.int)

#apply fourier transform
freq_signal = np.fft.fft(signal)

#normalization
freq_signal = abs(freq_signal[0:len_half])/len_signal

#square
freq_signal **=2

#extract lenght of the frequency transformed signal
len_fts = len(freq_signal)

#Adjust the signal for even/odd cases
if len_signal % 2:
    freq_signal[1:len_fts]*=2
else:
    freq_signal[1:len_fts-1]*=2

#extract the power value in dB
signal_power = 10 * np.log10(freq_signal)

#build x axis
x_axis = np.arange(0, len_half, 1) * (sampling_freq / len_signal)/1000.0

#plot the figure
plt.figure()
plt.plot(x_axis, signal_power, color='black')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Signal power(db)')
plt.show()