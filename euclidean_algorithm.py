class EuclideanAlgorithm:
    def __init__(self):
        self.a = None
        self.b = None

    def set_numbers(self, a, b):
        if a >= 0 and b >= 0:
            self.a = a
            self.b = b
        else:
            raise ValueError("Both numbers must be non-negative.")

    def compute_gcd(self):
        if self.a is None or self.b is None:
            raise ValueError("Numbers not set.")
        a, b = self.a, self.b
        while b != 0:
            a, b = b, a % b
        return a

def main():
    try:
        a = int(input("Enter the first number (non-negative): "))
        b = int(input("Enter the second number (non-negative): "))
        gcd_calculator = EuclideanAlgorithm()
        gcd_calculator.set_numbers(a, b)
        print("The GCD is:", gcd_calculator.compute_gcd())
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
