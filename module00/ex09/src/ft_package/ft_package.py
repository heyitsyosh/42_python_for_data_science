def count_in_list(lst: list, reference: str) -> int:
    """Counts how many times the target string appears in the list."""
    try:
        if not isinstance(reference, str):
            raise TypeError("'target' must be a string")
        if not isinstance(lst, list):
            raise TypeError("'items' must be a list")

        return lst.count(reference)
    except Exception as e:
        print("Error:", e)
