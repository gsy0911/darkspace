import matplotlib.pyplot as plt
import numpy as np
import rawpy
from scipy.interpolate import splrep, splev

from .utils import histogram


class Core:

    def __init__(self, file_path: str):
        self.raw = rawpy.imread(file_path)
        self.img: np.ndarray = self.raw.raw_image
        self.processed = self.raw.postprocess()
        self.processed_list = [{}]

    def show(self, width: int = 20, height: int = 8):
        rows = len(self.processed_list)
        fig, ax = plt.subplots(nrows=rows, ncols=2, facecolor='white', figsize=(width, height * rows))

        for idx, process_kwargs in enumerate(self.processed_list):
            img = self.raw.postprocess(**process_kwargs).copy()
            ax[idx, 0].set_title(f'{idx}: {process_kwargs}')
            ax[idx, 0].imshow(img)
            # plot color histogram
            self._histogram(img, ax[idx, 1])
        return None

    def add_process(self, **kwargs):
        self.processed_list.append(kwargs)
        return self

    def tone_curve(self, low: float, high: float):
        """

        Args:
            low: where 0 < low < 0.5
            high: where 0.5 < high < 1

        See Also:
            https://campkougaku.com/2020/01/15/rawpy-tone/

        Returns:

        """
        xs = [0, 0.25, 0.5, 0.75, 1]
        ys = [0, low, 0.5, high, 1]

        # spline
        tck = splrep(xs, ys)
        # normalization
        img = self.processed / 256
        # apply spline
        img = splev(img, tck)
        return img

    @staticmethod
    def _histogram(img: np.ndarray, ax):
        h_ax = np.arange(0, 256, 1)
        hist_r, _ = np.histogram(img[:, :, 0], bins=256, range=(0, 255))
        hist_g, _ = np.histogram(img[:, :, 1], bins=256, range=(0, 255))
        hist_b, _ = np.histogram(img[:, :, 2], bins=256, range=(0, 255))

        ax.bar(h_ax, hist_r, color='red', width=1, alpha=0.3)
        ax.bar(h_ax, hist_g, color='green', width=1, alpha=0.3)
        ax.bar(h_ax, hist_b, color='blue', width=1, alpha=0.3)
        return None

    def histogram(self):
        """

        Returns: histogram

        """
        return histogram(img=self.processed)
