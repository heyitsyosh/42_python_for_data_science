"""
Analyze a given text and print its statistics.
Usage:
    python building.py <text>
    python building.py"""

import sys
import string


def get_text_from_argv(args: list[str]) -> str:
    """Returns argv[1] if available, or prompts user for input."""
    assert len(args) < 2, "more than one argument is provided"
    if len(args) == 1:
        return args[0]
    print("What is the text to count?")
    return sys.stdin.readline()


def print_text_stats(text: str) -> None:
    """ Prints characteristics of the text. """
    print(f'The text contains {len(text)} characters:')
    print(sum(1 for c in text if c.isupper()), "upper letters")
    print(sum(1 for c in text if c.islower()), "lower letters")
    print(sum(1 for c in text if c in string.punctuation), "punctuation marks")
    print(sum(1 for c in text if c.isspace()), "spaces")
    print(sum(1 for c in text if c.isdigit()), "digits")


def main():
    try:
        print_text_stats(get_text_from_argv(sys.argv[1:]))
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
