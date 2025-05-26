import numpy as np
from scipy.signal import iirpeak, lfilter

def design_peak_filter(freq, fs, Q, gain_db):
    gain = 10 ** (gain_db / 20)
    b, a = iirpeak(freq / (fs / 2), Q)
    b *= gain
    return b, a

def apply_filters(signal, filters):
    for b, a in filters:
        signal = lfilter(b, a, signal)
    return signal