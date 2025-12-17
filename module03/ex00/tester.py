from S1E9 import Character, Stark


def printBlue(s): print("\033[34m{}\033[00m".format(s))


printBlue("Invalid tests:")
try:
    hodor = Character("hodor")
except Exception as e:
    print("Error:", e)

try:
    Catelyn = Stark()
except Exception as e:
    print("Error:", e)

printBlue("Valid tests:")
Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

# ---- [Expected output] ----
# {'first_name': 'Ned', 'is_alive': True}
# True
# False
# <Your docstring for Class>
# <Your docstring for Constructor>
# <Your docstring for Method>
# {'first_name': 'Lyanna', 'is_alive': False}
