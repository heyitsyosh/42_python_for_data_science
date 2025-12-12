from S1E9 import Character


class Baratheon(Character):
    """'Baratheon' class that inherits from 'Character'."""

    def __init__(self, first_name: str, is_alive: bool = True, ) -> None:
        """Initializes a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Returns a formatted string representation of the object."""
        return self.__repr__()

    def __repr__(self):
        """Returns a formatted string representation of the object."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    """'Lannister' class that inherits from 'Character'."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initializes a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Returns a formatted string representation of the object."""
        return self.__repr__()

    def __repr__(self):
        """Returns a formatted string representation of the object."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Creates and returns a new instance of class 'Lannister'."""
        return cls(first_name, is_alive)
