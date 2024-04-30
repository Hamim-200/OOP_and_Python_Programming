# def function_name();
#     return value


# Required Argument

def add(a, b, c):
    return a+b+c


print(add(1, 2, 3))


# Keyword Argument


def add(a, b, c):
    return a+b+c


print(add(b=10, a=2, c=3))

# Default Argument


def add(a, b, c=7):
    return a+b+c


print(add(b=10, a=2))


# Variable-Length Argument


def add(*args):
    print(type(args))
    sum = 0
    for i in args:
        sum = sum+i
    return sum


temp = add(1, 2, 3, 4, 5, 6, 7, 8)
print(temp)


# map

my_list = [2, 3, 4, 5, 6, 7]


def square(x):
    return x*x


new_list = map(square, my_list)
print(list(new_list))


# filter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(x):
    if x % 2 == 0:
        return True
    return False


temp = filter(is_even, my_list)
print(list(temp))
