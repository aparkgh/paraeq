from scipy.signal import iirpeak
import numpy as np

def design_peak_filter(freq, fs, Q, gain_db):
    gain = 10**(gain_db / 20)
    b, a = iirpeak(freq / (fs / 2), Q)
    b *= gain
    return b, a