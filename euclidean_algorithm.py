class EuclideanAlgorithm:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_gcd(self):
        """
        Compute the GCD of two numbers using the Euclidean Algorithm.

        Returns:
            int: The greatest common divisor of the initialized numbers.
        """
        a, b = self.a, self.b
        while b != 0:
            a, b = b, a % b
        return a
