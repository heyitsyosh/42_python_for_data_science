"""
Determine whether a given integer is even or odd.
Usage: python whatis.py <integer>"""

import sys


def what_is(num: int) -> str:
    return "even" if num % 2 == 0 else "odd"


def main(args: list[str]):
    assert len(args) < 2, "more than one argument is provided"
    if len(args) != 0:
        assert args[0].lstrip('-').isdigit(), "argument is not an integer"
        num = int(args[0])
        print(f"I'm {what_is(num)}.")
    print()


try:
    main(sys.argv[1:])
except AssertionError as e:
    print("AssertionError:", e)
