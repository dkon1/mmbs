# Lab 6 explore: time series frequency analysis

### Name

### Lab section

#Necessary imports
import numpy as np #package for work with arrays and matrices -- this week including some linear algebra
import matplotlib.pyplot as plt #package with plotting capabilities

import pandas as pd
pelts = pd.read_csv("pelt_data.csv")
pelts.head()

## Part 1: noise vs. signal

The following script generates a fake signal with periodic components and a noise term, performs a Fourier tranform and plots the power spectrum of the frequencies:

Fs = 60.0  # sampling rate
Ts = 1.0/Fs # sampling interval
Max_time = 2.0 # duration of the signal
t = np.arange(0,Max_time,Ts) # time vector
n = len(t) # length of time vector

# generate a signal with different frequencies
ff1 = 5   # frequency 1 of the signal
ff2 = 25   # frequency 2 of the signal
w1 = 5 # weight of frequency 1
w2 = 5 # weight of frequency 2
w3 = 2 # weight of noise
mu = 0 # mean value
sigma = 0.5 # standard deviation
fake_signal = w1*np.sin(2*np.pi*ff1*t)+ w2*np.sin(2*np.pi*ff2*t) + w3*np.random.normal(mu, sigma, n)

# frequency stuff
k = np.arange(n) # all the frequency indices
frq = k/Max_time  # two sides frequency range
num_freq = np.arange(np.ceil(n/2).astype(int)) # number of frequencies
frq = frq[num_freq] # non-redundant frequency range

# FFT and power spectrum calculations
Y = np.fft.fft(fake_signal)/n # fft computing and normalization
Y = Y[num_freq]
ps = np.abs(Y)**2 # power spectrum

# plotting the signal and the power spectrum
fig, ax = plt.subplots(2, 1)
ax[0].plot(t,fake_signal)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,ps[num_freq],'r') # plotting the power spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)^2|')
plt.show()

Experiment with the code above by increasing the noise weight (variable w3) and report what effect it has on the power spectrum. At what point does the power spectrum no longer have distinguishable frequency peaks for the two periodic components?

## Part 2: frequency spectrum of the hare and lynx pelt data

Plot the values of hare and lynx pelts contained in the pandas (data frame) pelts as a function of time (Hint: variables in pandas are accessed with a period. e.g. pandas.variable). Then perform Fourier frequency analysis of the two variables (using the above script as a template) and plot the power spectra. Describe the features of the power spectrum in terms of the dominant frequency and any trends or noise. 

pelts.Hare.shift(2)
slope, intercept, r, p_value, std_err = stats.linregress(pelts.Hare.shift(1), pelts.Hare.shif)
print("Model slope:    ", slope)
print("Model intercept:", intercept)
print("R^2:            ", r**2)



