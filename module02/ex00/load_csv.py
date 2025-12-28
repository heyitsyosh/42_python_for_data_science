import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads a dataset from the given path and returns it as a DataFrame."""
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df

    except FileNotFoundError:
        print(f"Error: file not found: '{path}'")
    except PermissionError:
        print(f"Error: permission denied: '{path}'")
    except pd.errors.ParserError:
        print(f"Error: invalid CSV format: '{path}'")
    except IsADirectoryError:
        print(f"Error: is a directory: '{path}'")
    except Exception as e:
        print("Error:", e)
