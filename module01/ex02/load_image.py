import cv2
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Loads an image and returns it as a NumPy array."""
    try:
        if not isinstance(path, str) or not cv2.haveImageReader(path):
            raise ValueError(f"'{path}' is an invalid filepath")
        img = cv2.imread(path, cv2.IMREAD_COLOR_RGB)
        if img is None:
            raise ValueError(f"failed to read image at '{path}'")
        print("The shape of the image is:", img.shape)
        return img
    except Exception as e:
        print("Error:", e)
