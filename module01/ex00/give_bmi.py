import numpy as np


def validate_list(my_list: list[int | float], name: str):
    """Validate that the list contains only positive ints/floats."""
    if not isinstance(my_list, list):
        raise TypeError(f'{name} must be given in list format.')
    for x in my_list:
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError(f'{name} must contain only numeric values.')
        if x <= 0:
            raise ValueError(f'{name} contains zero or negative values.')


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculates BMIs from heights(m) and weights(kg).
    BMI = weight(kg) / height(m^2)
    """
    try:
        validate_list(height, "height")
        validate_list(weight, "weight")
        if len(height) != len(weight):
            raise ValueError("height and weight must have the same length.")

        heights = np.asarray(height)
        weights = np.asarray(weight)

        bmi_arr = weights / heights ** 2
        return bmi_arr.tolist()
    except Exception as e:
        print(f'Error: {e}')


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compares list of BMIs against a given limit.
    Returns a list of booleans where True indicates the BMI exceeds the limit.
    """
    try:
        validate_list(bmi, "bmi")
        limit_f = float(limit)
        return [b > limit_f for b in bmi]
    except Exception as e:
        print(f'Error: {e}')
