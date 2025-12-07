from load_image import ft_load
from pimp_image import show, ft_invert, ft_red, ft_green, ft_blue, ft_gray

array = ft_load("../assets/landscape.jpg")

show(array, "Original ver.")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_gray(array)

print(ft_invert.__doc__)
