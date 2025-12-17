class calculator:
    """'calculator' class that overloads operators for vectors."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiplies two vectors together."""
        result = 0
        for i in range(len((V1))):
            result += V1[i] * V2[i]
        print("Dot product is:", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds two vectors together."""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts one vector from another vector."""
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is:", result)
