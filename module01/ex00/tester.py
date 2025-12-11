from give_bmi import give_bmi, apply_limit


def printBlue(s): print("\033[34m{}\033[00m".format(s))


height = [2.71, 1.15]
weight = [165.3, 38.4]

printBlue("Invalid tests:")
give_bmi(3, weight)
give_bmi([2.71, 1.15, 3], weight)
give_bmi([2.71, False], weight)
give_bmi([2.71, "a"], weight)
give_bmi([2.71, 0], weight)

printBlue("Valid tests:")
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# ---- [Expected valid output] ----
# [22.507863455018317, 29.0359168241966] <class 'list'>
# [False, True]
