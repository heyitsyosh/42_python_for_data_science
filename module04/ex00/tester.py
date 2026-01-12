from statistics import ft_statistics

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(1, 2, tata="quartile")
ft_statistics(1, 2, 3, tata="quartile")
ft_statistics(1, 2, 3, 4, 5, 6, 7, tata="quartile")
ft_statistics(1, 2, 3, 4, 5, 6, 7, 8, tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
              ejfhhe="heheh", ejdjdejn="kdekem")
ft_statistics(toto="mean", tutu="median", tata="quartile")

# ---- [Expected output] ----
# mean : 95.6
# median : 42
# quartile : [11.0, 64.0]
# ----
# std : 17982.70124086944
# var : 323377543.9183673
# ---------
# ERROR_MSG
# ERROR_MSG
# ERROR_MSG
