from load_image import ft_load


def printBlue(s): print("\033[34m{}\033[00m".format(s))


printBlue("Invalid tests:")
ft_load("")
ft_load(3)
ft_load("../assets/landscape.jp")
ft_load("../assets/nonexistent.jpg")
ft_load("../assets/test.pdf")
# ft_load("../assets/nopermissions.jpg")

printBlue("Valid tests:")
print(ft_load("../assets/landscape.jpg"))

# ---- [Expected valid output] ----
# The shape of image is: (257, 450, 3)
# [[[19 42 83]
# [23 42 84]
# [28 43 84]
# ...
# [ 0 0 0]
# [ 1 1 1]
# [ 1 1 1]]]
