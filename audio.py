import sounddevice as sd
import numpy as np
from dsp import apply_filters, design_peak_filter

class AudioEngine:
    def __init__(self, eq_settings, fs=44100):
        self.fs = fs
        self.eq_settings = eq_settings
        self.stream = sd.Stream(callback=self.callback, samplerate=fs, channels=1)

    def callback(self, indata, outdata, frames, time, status):
        signal = indata[:, 0]
        filters = [design_peak_filter(f, self.fs, q, g)
                   for (f, g, q) in self.eq_settings()]
        out = apply_filters(signal, filters)
        outdata[:, 0] = out

    def start(self):
        self.stream.start()

    def stop(self):
        self.stream.stop()