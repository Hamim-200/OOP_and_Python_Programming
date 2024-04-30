# def full_name(first,last):
#     name = f'{first} {last}'
#     return name

# Take parameters in order
# name = full_name('Alu','Khan')
# name = full_name(last='kodu',first='alu')
# print(name)


# def famous_name(first,last,title,addition):
#     name = f'{title} {first} {last} {addition}'
#     return name
# name = famous_name(first='Taher', last='Ali' ,title='Hujur', addition='Taheriiii')
# print(name)


def example_function(a, b, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(1, 2, name="Alice", age=30, city="New York")
