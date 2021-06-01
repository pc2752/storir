import tkinter
import matplotlib
matplotlib.use('TkAgg')
from storir import ImpulseResponse
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # example configuration
    rt60 = 1000
    edt = 50
    itdg = 3
    er_duration = 80
    drr = -5
    sr = 16000

    rir = ImpulseResponse(rt60=rt60,
                          edt=edt,
                          itdg=itdg,
                          drr=drr,
                          er_duration=er_duration)

    # get 5 impulse responses
    for _ in range(5):
        output = rir.generate(sampling_rate=sr)
        plt.plot(output)
        plt.show()
        print(output.shape)
