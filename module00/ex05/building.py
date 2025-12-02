import sys
import string


def get_text_from_argv(argv: list[str]) -> str:
    """Return argv[1] if provided, otherwise prompt the user for input."""
    assert len(argv) <= 2, "more than one argument is provided"
    if len(argv) == 2:
        return argv[1]
    print("What is the text to count?")
    return sys.stdin.readline()


def print_text_stats(text: str):
    """ Prints characteristics of the text. """
    print(f'The text contains {len(text)} characters:')
    print(sum(1 for c in text if c.isupper()), "upper letters")
    print(sum(1 for c in text if c.islower()), "lower letters")
    print(sum(1 for c in text if c in string.punctuation), "punctuation marks")
    print(sum(1 for c in text if c.isspace()), "spaces")
    print(sum(1 for c in text if c.isdigit()), "digits")


def main():
    try:
        print_text_stats(get_text_from_argv(sys.argv))
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
