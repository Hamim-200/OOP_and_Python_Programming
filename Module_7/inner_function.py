def double_decker():
    print('Starting the double decker')

    def inner_fun():
        print('Inside the inner function')
        return 3000

    return inner_fun

# print(double_decker())
print(double_decker()())