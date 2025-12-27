"""
Crop, rotate, and convert an image to grayscale.
Usage: rotate.py"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(img: np.ndarray,
         height: int = 400,
         width: int = 400,
         starting_pixel: tuple[int, int] = (450, 100)
         ) -> np.ndarray:
    """Returns a cropped region of `img` of size (height, width).
The crop begins at the specified top-left starting pixel (x, y)."""
    x, y = starting_pixel  # top-left pixel coordinates
    h, w = img.shape[:2]
    if x < 0 or y < 0 or y >= h or x >= w:
        raise ValueError("Starting pixel is outside image bounds")
    return img[y:y+height, x:x+width]


def to_grayscale(img: np.ndarray) -> np.ndarray:
    """Converts an RGB image array to grayscale using OpenCV."""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def transpose(img: np.ndarray) -> np.ndarray:
    """Transposes/rotates an image"""
    rows, cols = img.shape[:2]
    transposed_img = np.empty((cols, rows), dtype=img.dtype)

    for row in range(rows):
        for col in range(cols):
            transposed_img[col, row] = img[row, col]

    return transposed_img


def show(img: np.ndarray) -> None:
    """Displays an image array using matplotlib."""
    plt.imshow(img, cmap='gray')
    plt.show()


def print_as_3d(img: np.ndarray) -> None:
    """
    Normalizes the input to a 3D array.
    Then outputs its shape and contents.
    """
    img_3d = np.atleast_3d(img)  # Ensure image has a (H, W, 1) shape
    print(f'The shape of the image is: {img_3d.shape} or {img.shape[:2]}')
    print(img_3d)


def main():
    try:
        path = "../assets/animal.jpeg"

        img = ft_load(path)
        processed_img = to_grayscale(zoom(img))
        print_as_3d(processed_img)

        transposed_img = transpose(processed_img)
        show(transposed_img)

        print(f'New shape after Transpose: {transposed_img.shape}')
        print(transposed_img)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
