import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """'Student' class. Requires name and surname parameters."""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> None:
        """Generates a login from the student's name and surname."""
        self.login = (self.name[:1] + self.surname)[:8]
