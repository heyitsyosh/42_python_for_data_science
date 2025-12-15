import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D 'family' list between start and end indices.
Prints the initial shape and the shape after slicing."""
    try:
        if not isinstance(family, list):
            raise TypeError("'family' must be in list format")
        if not isinstance(start, int):
            raise TypeError("'start' must be an integer")
        if not isinstance(end, int):
            raise TypeError("'end' must be an integer")
        if any(not isinstance(row, list) for row in family):
            raise TypeError("'family' must contain only lists")
        if family and any(len(row) != len(family[0]) for row in family):
            raise ValueError("lists in 'family' must have equa lengths")

        array = np.asarray(family)
        print(f'My shape is: {array.shape}')
        sliced = array[start:end]
        print(f'My new shape is: {sliced.shape}')

        return sliced.tolist()
    except Exception as e:
        print("Error:", e)
