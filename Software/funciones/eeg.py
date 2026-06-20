import numpy as np
from scipy.signal import welch
from funciones.filtros import bandpass

FS=1000

def alpha_power(segmento):

    eeg=bandpass(
        segmento,
        1,
        40,
        FS
    )

    freqs,psd=welch(
        eeg,
        fs=FS
    )

    mask=(freqs>=8)&(freqs<=13)

    return np.trapezoid(
        psd[mask],
        freqs[mask]
    )
