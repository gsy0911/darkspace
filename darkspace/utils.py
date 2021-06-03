import matplotlib.pyplot as plt
import numpy as np


def histogram(img: np.ndarray):
    # https://campkougaku.com/2019/12/05/rawpy6/
    h_ax = np.arange(0, 256, 1)
    hist_r, _ = np.histogram(img[:, :, 0], bins=256, range=(0, 255))
    hist_g, _ = np.histogram(img[:, :, 1], bins=256, range=(0, 255))
    hist_b, _ = np.histogram(img[:, :, 2], bins=256, range=(0, 255))

    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(xlabel='8Bit Luminance', ylabel='count', xlim=(0, 255), title='RGB histgram')
    ax.bar(h_ax, hist_r, color='red', width=1, alpha=0.3)
    ax.bar(h_ax, hist_g, color='green', width=1, alpha=0.3)
    ax.bar(h_ax, hist_b, color='blue', width=1, alpha=0.3)
    return fig
