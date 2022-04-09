import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import IPython.display as ipd


def espectro(y, name="default", Fs=1):

    # modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))

    N = Y.size  # Number of samplepoints
    T = 1.0 / Fs  # N_samps*T (#samples x sample period) is the sample spacing.
    x = np.linspace(0, N * T, N)

    # frequencias avaliadas
    # w = np.arange(-Y.size / 2, Y.size / 2)
    w = np.linspace(0, N * T, Y.size)
    # w = np.linspace(-Y.size/2,Y.size/2,Y.size)
    # w = np.linspace()

    # exibe o grafico do espectro
    plt.figure(figsize=[14, 4])
    plt.plot(w, Y / np.max(Y))
    plt.xlabel("Hz", fontsize=15)
    plt.xlim(0, N / 2)
    # plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=15)

    plt.grid(True)

    if name != "default":
        plt.savefig(f"{name}.png")

    return Y
