"""Display a scatter plot where each point represents a country.

The x-axis shows GDP per capita.
The y-axis shows life expectancy.
Each point is calculated using data from the year 1900."""

from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        year = "1900"
        life_expectancy_data = load("../data/life_expectancy_years.csv")
        gdp_data = load("../data/income_per_person_gdppercapita_"
                        "ppp_inflation_adjusted.csv")

        plt.scatter(gdp_data[year], life_expectancy_data[year])

        ax = plt.subplot()
        ax.set(
            xlabel="Gross Domestic Product",
            ylabel="Life Expectancy",
            xscale="log",
            title=year,
            xticks=[300, 1000, 10000]
        )
        ax.xaxis.set_major_formatter(
            lambda x, pos: f'{x/1000:g}k' if x >= 1000 else x
        )
        plt.show()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
