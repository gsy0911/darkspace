from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import rawpy

from .utils import histogram


class Core:

    def __init__(self, file_path: str):
        self.raw = rawpy.imread(file_path)
        self.img: np.ndarray = self.raw.raw_image
        self.processed = self.raw.postprocess()
        self.processed_list = [self.processed.copy()]

    def show(self, figsize: Tuple[int, int] = (10, 32)):
        fig = plt.figure(facecolor='white', figsize=figsize)
        for idx, img in enumerate(self.processed_list):
            ax = plt.subplot(411+idx, title=f'{idx}: ')
            ax = plt.imshow(img)
        return None

    def postprocess(self, **kwargs):
        self.processed = self.raw.postprocess(**kwargs)
        self.processed_list.append(self.processed.copy())
        return self

    def histogram(self):
        """

        Returns: histogram

        """
        return histogram(img=self.processed)
