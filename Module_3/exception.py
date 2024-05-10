try:
    x = 1 / 0
except:
    print("Cannot divide by zero!")


try:
    x = "hello" + 5
except TypeError:
    print("Cannot concatenate string and integer!")


try:
    x = int("hello")
except ValueError:
    print("Cannot convert 'hello' to an integer!")
