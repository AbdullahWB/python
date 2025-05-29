import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)

# Example Usage
num = float(input("Enter a number: "))
calc = Calculator(num)

print(f"Square of {num}: {calc.square()}")
print(f"Cube of {num}: {calc.cube()}")
print(f"Square Root of {num}: {round(calc.square_root(), 2)}")
