import os


def small_bar(ratio: float) -> None:
    """Returns a Unicode block character representing progress."""
    blocks = [" ", "▏", "▎", "▍", "▋", "▊", "▉", "█"]
    i = min(int(ratio * len(blocks)), len(blocks) - 1)
    return blocks[i]


def ft_tqdm(lst: range) -> None:  # type: ignore
    """Self implementation of tqdm (https://github.com/tqdm/tqdm).
A progressbar decorator for iterators."""
    lst_len = len(lst)
    counter_width = len(str(len(lst))) * 2 + 1
    bar_width = (os.get_terminal_size().columns - counter_width - 33)

    for i, item in enumerate(lst, start=1):
        ratio = i / lst_len
        if bar_width < 1:
            bar = small_bar(ratio)
        else:
            filled = int(ratio * bar_width)
            bar = "█" * filled + " " * (bar_width - filled)
        print(f"\r{ratio * 100:3.0f}%|{bar}| {i}/{lst_len}", end='')
        yield
