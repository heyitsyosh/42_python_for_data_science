ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# LIST — ordered, mutable
ft_list[1] = "World!"

# TUPLE — ordered, immutable
ft_tuple = ("Hello", "France!")

# SET — unordered, mutable
ft_set.discard("tutu!")
ft_set.add("Paris!")

# DICTIONARY — ordered (Python 3.7+), mutable
ft_dict.update({"Hello": "42Paris!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
