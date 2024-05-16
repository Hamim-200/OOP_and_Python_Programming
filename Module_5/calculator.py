class Calculator:
    brand = 'Casio MS909'

    def add (self,num1,num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."


calc = Calculator()
print(calc.add(10, 5))  # Output: 15
print(calc.subtract(10, 5))  # Output: 5
print(calc.multiply(10, 5))  # Output: 50
print(calc.divide(10, 5))  # Output: 2.0
print(calc.divide(10, 0))  # Output: Error: Division by zero is not allowed.