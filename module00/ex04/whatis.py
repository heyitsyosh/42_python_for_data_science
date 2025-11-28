import sys


def what_is(num: int) -> str:
    return "even" if num % 2 == 0 else "odd"


def main(argv: list[str]):
    if len(argv) == 1:
        return
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")
    if not argv[1].lstrip('-').isdigit():
        raise AssertionError("argument is not an integer")
    num = int(argv[1])
    print(f"I'm {what_is(num)}.")


try:
    main(sys.argv)
except AssertionError as e:
    print(f'AssertionError: {e}')
