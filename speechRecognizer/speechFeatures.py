#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc, logfbank

#Read the input audo file
sampling_freq, signal = wavfile.read('hello.wav')

#take first 10,000 samples for analysis
signal = signal[:10000]

#extract mfcc features (Mel Frequency Cepstral Coefficients)
features_mfcc = mfcc(signal, sampling_freq)

#print the paramaters for mfcc
print('\nMFCC:\nNumber of windows =', features_mfcc.shape[0])
print('Length of each feature =',features_mfcc.shape[1])

#plot the features
features_mfcc = features_mfcc.T
plt.matshow(features_mfcc)
plt.title('MFCC')

#extract the filter bank features
features_fb = logfbank(signal, sampling_freq)

#print the params for filter bank
print('\nFilter bank:\nNumber of windows=',features_fb.shape[0])
print('Length of each feature =', features_fb.shape[1])

#Plot the features
features_fb = features_fb.T
plt.matshow(features_fb)
plt.title('Filter bank')
plt.show()