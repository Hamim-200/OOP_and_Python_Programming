def sum(num1,num2,num3=0):
    result = num1+num2+num3
    return result

# total = sum(99,11)
# print('Total :',total)

# args

def all_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum

total = all_sum(45,5,21,23,2,35,43)
print('All Sum',total)    