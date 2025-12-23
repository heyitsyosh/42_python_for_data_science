"""Docstring for module02.ex01.aff_life
"""

from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("../data/life_expectancy_years.csv")
    if df is None:
        return

    df.loc[df["country"] == "France"]



if __name__ == "__main__":
    main()
