import numpy as np
# pip install numpy


def validate_list_to_array(
    my_list: list[int | float],
    name: str
) -> np.ndarray:
    """Validate numeric values and return them as a NumPy array."""
    if not isinstance(my_list, list):
        raise TypeError(f"{name} must be given in list format.")
    if any(isinstance(x, bool) for x in my_list):
        raise TypeError(f"{name} must not contain boolean values.")

    array = np.asarray(my_list)

    if not np.issubdtype(array.dtype, np.number):
        raise TypeError(f"{name} must contain only numeric values.")
    if (array <= 0).any():
        raise ValueError(f"{name} contains zero or negative values.")

    return array


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculates BMIs from heights(m) and weights(kg).
    BMI = weight(kg) / height(m^2)
    """
    try:
        heights = validate_list_to_array(height, "height")
        weights = validate_list_to_array(weight, "weight")
        if heights.size != weights.size:
            raise ValueError("height and weight must have the same length.")
        bmi_arr = weights / heights ** 2
        return bmi_arr.tolist()
    except Exception as e:
        print(f'Error: {e}')


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """"""
