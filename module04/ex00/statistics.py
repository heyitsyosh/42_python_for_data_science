from typing import Any


def validate_and_convert_to_list(args: tuple[Any, ...]) -> list[float]:
    """Validates that dataset only contains numbers.
Then returns the dataset as a list."""
    if len(args) == 0:
        raise ValueError("no dataset provided")
    ret = []
    for x in args:
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError("dataset must contain only numbers")
        ret.append(x)
    return ret


def ft_mean(data: list[int | float]) -> int | float:
    """Returns the mean."""
    return sum(data) / len(data)


def is_even(n: int) -> bool:
    if n & 1:
        return False
    else:
        return True


def ft_median(data: list[int | float]) -> int | float:
    """Returns the median."""
    middle = len(data) // 2
    sorted_data = sorted(data)
    if is_even(len(data)):
        return ft_mean(sorted_data[middle - 1: middle + 1])
    return sorted_data[middle]


def ft_quartile(data: list[int | float]) -> int | float:
    """Returns the values at the lower and upper quartile indices."""
    if len(data) < 2:
        raise ValueError('dataset too small for quartiles')

    sorted_data = sorted(data)
    q1 = sorted_data[int(len(data) / 4)]
    q3 = sorted_data[int(3 * len(data) / 4)]

    return [q1, q3]


def ft_variance(data: list[int | float]) -> int | float:
    """Returns the variance."""
    mean = ft_mean(data)
    return sum(((x - mean) ** 2 for x in data)) / len(data)


def ft_std(data: list[int | float]) -> int | float:
    """Returns the standard deviation."""
    return ft_variance(data) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Computes and displays statistical measures for a dataset.

Parameters:
    *args    - contains the dataset (numbers only).
    **kwargs - specifies which statistics to print.
               (e.g. "mean", "median", "quartile", "std", "var").

Example:
    ft_statistics(1, 2, 3, 4, a="mean", b="median")"""
    try:
        data = validate_and_convert_to_list(args)
        for _, value in kwargs.items():
            match value:
                case "mean":
                    print(f'mean : {ft_mean(data)}')
                case "median":
                    print(f'mean : {ft_median(data)}')
                case "quartile":
                    quartiles = ft_quartile(data)
                    print(f'quartile : {[float(x) for x in quartiles]}')
                case "std":
                    print(f'std : {ft_std(data)}')
                case "var":
                    print(f'var : {ft_variance(data)}')
                case _:
                    raise ValueError(f"'{value}' is an invalid measure")
    except Exception as e:
        print("Error:", e)
