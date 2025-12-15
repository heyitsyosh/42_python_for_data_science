"""
Filter words in a text by minimum length.
Usage: python filterstring.py <text> <min_length>"""

import sys
from ft_filter import ft_filter


def validate_args(args: list[str]) -> None:
    """Validates that arguments are given correctly.
    String with no special characters, integer"""
    assert len(args) == 2, f'expected 2 arguments, got {len(args)}'
    assert all(c.isalnum() or c == ' ' for c in args[0]), \
        "first argument contains special characters"
    try:
        int(args[1])
    except ValueError:
        assert False, f'second argument must be an integer, got {args[1]!r}'


def filterstring(string: str, min_length: int):
    """Returns words longer than the given minimum length"""
    words = [word for word in string.split()]
    return ft_filter(lambda word: len(word) > min_length, words)


def main():
    try:
        validate_args(sys.argv[1:])
        filtered = filterstring(sys.argv[1], int(sys.argv[2]))
        print(list(filtered))
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
