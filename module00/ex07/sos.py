import sys


def validate_argv(argv: list[str]) -> None:
    """Validates that argv contains a single alphanumeric argument string."""
    assert len(argv) == 2, "wrong number of arguments, must be one"
    assert all(ch.isalnum() or ch == ' ' for ch in argv[1]), \
        "only alphanumeric characters are allowed"


def encode_to_morse(string: str) -> str:
    """Encodes the string into morse code"""
    morse_dict = {
        " ": "/",
        # Alphabet
        "A": ".-", "B": "-...", "C": "-.-.",
        "D": "-..", "E": ".", "F": "..-.",
        "G": "--.", "H": "....", "I": "..",
        "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.",
        "S": "...", "T": "-", "U": "..-",
        "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    encoded = []
    for ch in string.upper():
        encoded.append(morse_dict[ch])
    return ' '.join(encoded)


def main():
    if len(sys.argv) < 2:
        return
    try:
        validate_argv(sys.argv)
        morse_translation = encode_to_morse(sys.argv[1])
        print(morse_translation)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
