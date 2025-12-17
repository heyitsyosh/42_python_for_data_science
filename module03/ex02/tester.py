from DiamondTrap import King
from S1E9 import Character

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

# Print method resolution order
print("mro:", type(Joffrey).__mro__)

character = Character("Character")
Joffrey = character
print(Joffrey.__dict__)
