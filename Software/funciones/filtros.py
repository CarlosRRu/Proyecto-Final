from scipy.signal import butter,filtfilt

def bandpass(signal,low,high,fs,order=4):

    nyq=fs/2

    b,a=butter(
        order,
        [low/nyq,high/nyq],
        btype="band"
    )

    return filtfilt(
        b,
        a,
        signal
    )
