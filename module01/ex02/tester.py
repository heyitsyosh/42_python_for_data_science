from load_image import ft_load


def printBlue(s): print("\033[34m{}\033[00m".format(s))


printBlue("Invalid tests:")
ft_load("")
ft_load(3)
ft_load("../assets/landscape.jp")
ft_load("../assets/nonexistent.jpg")
ft_load("../assets/test.pdf")
# ft_load("../assets/nopermissions.jpg")

printBlue("Valid test(s):")
print(ft_load("../assets/landscape.jpg"))
