import numpy as np
import matplotlib.pyplot as plt


def show(img: np.ndarray, window_name: str) -> None:
    """Displays an image in a titled matplotlib window."""
    fig = plt.figure()
    fig.canvas.manager.set_window_title(window_name)

    cmap_settings = None
    if img.ndim < 3 or img.shape[2] == 1:
        cmap_settings = "gray"
    plt.imshow(img, cmap=cmap_settings)
    plt.axis("off")
    plt.show()


def ft_invert(original_img: np.ndarray) -> np.ndarray:
    """Inverts the colors of an image."""
    try:
        if not isinstance(original_img, np.ndarray):
            raise TypeError("image must be given in array format")

        inverted_img = 255 - original_img
        show(inverted_img, "Inverted ver.")

        return inverted_img
    except Exception as e:
        print("Error:", e)


def ft_red(original_img: np.ndarray) -> np.ndarray:
    """Applies a red filter to an image."""
    try:
        if not isinstance(original_img, np.ndarray):
            raise TypeError("image must be given in array format")
        
        red_img = original_img.copy()
        red_img[:, :, (1, 2)] = 0
        show(red_img, "Red ver.")

        return red_img
    except Exception as e:
        print("Error:", e)


def ft_green(original_img: np.ndarray) -> np.ndarray:
    """Applies a green filter to an image."""
    try:
        if not isinstance(original_img, np.ndarray):
            raise TypeError("image must be given in array format")

        green_img = original_img.copy()
        green_img[:, :, (0, 2)] = 0
        show(green_img, "Green ver.")

        return green_img
    except Exception as e:
        print("Error:", e)


def ft_blue(original_img: np.ndarray) -> np.ndarray:
    """Applies a blue filter to an image."""
    try:
        if not isinstance(original_img, np.ndarray):
            raise TypeError("image must be given in array format")

        blue_img = original_img.copy()
        blue_img[:, :, (0, 1)] = 0
        show(blue_img, "Blue ver.")

        return blue_img
    except Exception as e:
        print("Error:", e)


def ft_gray(original_img: np.ndarray) -> np.ndarray:
    """Applies a grayscale filter to an image."""
    try:
        if not isinstance(original_img, np.ndarray):
            raise TypeError("image must be given in array format")

        gray_img = np.dot(original_img[..., :3], [0.2989, 0.5870, 0.1140])
        show(gray_img, "Gray ver.")

        return gray_img
    except Exception as e:
        print("Error:", e)
