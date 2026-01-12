from typing import Any


def callLimit(limit: int) -> object:
    """Decorator factory."""
    count = 0

    def callLimiter(function):
        """Decorator."""
        def limit_function(*args: Any, **kwargs: Any):
            """Wrapper that enforces the call limit."""
            nonlocal count
            count += 1
            if count > limit:
                print("Error:", function, "was called too many times")
                return None
            return function(*args, **kwargs)
        return limit_function
    return callLimiter
