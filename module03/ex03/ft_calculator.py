class calculator:
    """'calculator' class that overloads operators for vectors."""
    def __init__(self, vector: list) -> None:
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds vector and scalar together."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplies vector and scalar together."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtracts scalar from vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divides vector by scalar."""
        try:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError:
            print("Error: division by zero is not allowed")
