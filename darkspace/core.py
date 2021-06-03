import numpy as np
import rawpy

from .utils import histogram


class Core:

    def __init__(self, file_path: str):
        self.raw = rawpy.imread(file_path)
        self.img: np.ndarray = self.raw.raw_image
        self.processed = self.raw.postprocess()

    def histogram(self):
        """

        Returns: histogram

        """
        return histogram(img=self.processed)
