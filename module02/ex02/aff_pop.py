"""Visualize population projections for two countries.
Data is extracted from a CSV containing population by country and year."""

from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes  # for type hint
import matplotlib.ticker as ticker


def normalize_value(v: str | int) -> float:
    """Converts values suffixed with 'k' or 'M' to float.
'k' represents thousands. 'M' represents millions."""
    if isinstance(v, str) and v.endswith('k'):
        return float(v[:-1]) * 1_000
    elif isinstance(v, str) and v.endswith('M'):
        return float(v[:-1]) * 1_000_000
    else:
        return float(v)


def plot_country_data(country: str,
                      df: pd.DataFrame,
                      ax: Axes) -> None:
    """Plots population data for one country."""
    country_data = df.loc[df["country"] == country].squeeze()

    x = df.columns[1:]
    y = country_data.iloc[1:].apply(normalize_value)
    color = "green" if country == "France" else "steelblue"

    ax.plot(x, y, color, label=country)


def customize_graph_display(ax: Axes) -> None:
    """Configures title, axes labels, ticks, and legend."""
    ax.set(
        xlabel="Year",
        ylabel="Population",
        title="Population Projections"
    )
    ax.legend(loc="lower right")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
    _, ymax_ = ax.get_ylim()
    if ymax_ >= 1_000_000:
        ax.yaxis.set_major_formatter(
            lambda x, _: f"{x/1_000_000:.0f}M"
        )


def main():
    try:
        path = "../data/population_total.csv"
        df = load(path)
        df = df.iloc[:, :252]  # 252 = (2051 - 1800) + 1

        country1 = "Belgium"
        country2 = "France"

        ax = plt.subplot()
        plot_country_data(country1, df, ax)
        plot_country_data(country2, df, ax)
        customize_graph_display(ax)
        plt.show()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
