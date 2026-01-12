from load_csv import load


def printBlue(s): print("\033[34m{}\033[00m".format(s))


printBlue("Valid tests:")
print(load("../data/life_expectancy_years.csv"))

printBlue("\nInvalid tests:")
load("3")
load(None)
load("")
load(".")
load("../data/bad.csv")
load("../data/empty.csv")
# load("../data/no_permission.csv")
