import sys


def what_is(num: int) -> str:
    return "even" if num % 2 == 0 else "odd"


def main(args: list[str]):
    if len(args) == 0:
        return
    assert len(args) < 2, "more than one argument is provided"
    assert args[0].lstrip('-').isdigit(), "argument is not an integer"
    num = int(args[0])
    print(f"I'm {what_is(num)}.")


try:
    main(sys.argv[1:])
except AssertionError as e:
    print("AssertionError:", e)
