import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """Loads a dataset from the given path and returns it as a DataFrame."""
    df = pd.read_csv(path)
    print("Loading dataset of dimensions", df.shape)
    return df
