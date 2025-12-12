from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """'King' class that inherits from 'Baratheon' and 'Lannister'."""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initializes a King character."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str) -> None:
        """Sets the eye color."""
        self.eyes = color

    def set_hairs(self, color: str) -> None:
        """Sets the hair color."""
        self.hairs = color

    def get_eyes(self) -> str:
        """Returns the eye color."""
        return self.eyes

    def get_hairs(self) -> str:
        """Returns the hair color."""
        return self.hairs
