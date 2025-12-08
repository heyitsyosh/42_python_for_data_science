from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class named 'Character'."""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Character class constructor.
        Initializes first_name (str) and is_alive (bool) status.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method 'die' to be implemented by subclasses."""
        pass


class Stark(Character):
    """Inherited class named 'Stark'"""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Stark class constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Sets the is_alive parameter to false."""
        self.is_alive = False
