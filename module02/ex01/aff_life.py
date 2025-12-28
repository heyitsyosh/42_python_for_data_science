"""Visualize life expectancy projections for France.
Data is extracted from a CSV containing life expectancy by country and year."""

from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def visualize_france_data(df: pd.DataFrame) -> None:
    """"Plots France's life expectancy over time."""
    ax = plt.subplot()
    france_data = df.loc[df["country"] == "France"]
    ax.plot(df.columns[1:], france_data.iloc[0, 1:])
    ax.set(
        xlabel="Year",
        ylabel="Life expectancy",
        title="France Life Expectancy Projections"
    )
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    plt.show()


def main():
    try:
        path = "../data/life_expectancy_years.csv"
        df = load(path)
        visualize_france_data(df)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
