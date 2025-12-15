from abc import ABC


class Character(ABC):
    """Abstract base class named 'Character'."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initializes a character."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """Sets the is_alive parameter to false."""
        self.is_alive = False


class Stark(Character):
    """'Stark' class that inherits from 'Character'."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initializes a Stark character."""
        super().__init__(first_name, is_alive)
