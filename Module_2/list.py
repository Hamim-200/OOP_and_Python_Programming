# List, Array , collection 

#index  =  0   1   2   3   4   5  6  7  8   9
numbers = [45, 23, 21, 34, 56, 3, 2, 1, 98, 32]
#index  =  -10  -9 -8  -7  -6  -5 -4 -3 -2  -1

print(numbers[3], numbers[-3])

print(numbers[1:5])

#list(start : end : step)
print(numbers[1:7:2])
print(numbers[2:7:-1])
print(numbers[4:])
print(numbers[:7])
print(numbers[:]) #Shortcut to copy a list
print(numbers[::-1]) # Shortcut Reverse