# define

def double_it(num):
    result = num * 2
    print(result)
    return result

double_it(10)
double_it(20)
double_it(15)


def multiply_it(num1, num2):
    result = num1 * num2
    return result

total = multiply_it(10,20)
print('Total It',total)

final = double_it(total)
print('Final Value',final)