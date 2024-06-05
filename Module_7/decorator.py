import math
import time

def timer (func):
    def inner(*args, **kwargs):
        print('Time started')
        start = time.time()
        # print(func)
        func(*args,**kwargs)
        print('time ended')
        end = time.time()
        print(f'Total time taken{end-start}')
    return inner


@timer
def get_factorial(n):
    print('Factorial starting')
    result = math.factorial(n)
    print(f'Factorial of {n} is : {result}')

get_factorial(n=12)