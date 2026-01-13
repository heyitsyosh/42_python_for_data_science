from typing import Callable


def square(x: int | float) -> int | float:
    """Returns the square of a number."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns a number raised to the power of itself."""
    return x ** x


def outer(x: int | float, function: Callable) -> Callable:
    """Creates a closure that lets 'count' persist between calls."""
    count = 0

    def inner() -> int | float:
        """Applies 'function' to 'x' as many times as the call count."""
        nonlocal count
        result = function(x)
        for _ in range(count):
            result = function(result)
        count += 1
        return float(result)
    return inner
