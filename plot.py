import matplotlib.pyplot as plt
from scipy.signal import freqz
from dsp import design_peak_filter

def plot_response(bands, fs=44100):
    w = np.linspace(0, fs / 2, 800)
    h_total = np.ones_like(w, dtype=complex)

    for f, g, q in bands:
        b, a = design_peak_filter(f, fs, q, g)
        w_, h = freqz(b, a, worN=w, fs=fs)
        h_total *= h

    plt.figure()
    plt.semilogx(w, 20 * np.log10(np.abs(h_total)))
    plt.title('EQ Frequency Response')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Gain [dB]')
    plt.grid(which='both', linestyle='--')
    plt.show()