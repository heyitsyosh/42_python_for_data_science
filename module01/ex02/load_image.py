from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Loads an image and returns it as a NumPy array."""
    try:
        if not isinstance(path, str):
            raise ValueError(f"'{path}' is an invalid filepath")
        img = Image.open(path)
        img_arr = np.array(img)
        print("The shape of the image is:", img_arr.shape)
        return img_arr
    except Exception as e:
        print("Error:", e)
