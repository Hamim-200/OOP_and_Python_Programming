numbers = [45, 28, 21, 34, 56, 3, 2, 1, 98, 32,75]
odds = []
for num in numbers:
    if num in numbers:
        if num % 2 == 1 and num % 5 == 0:
            odds.append(num)
print(odds)            

odd_nums = [num for num in numbers if num % 2 == 1]
print('Second odd Number', odd_nums)

strings = ["hello", "world", "python"]
uppercase_strings = [s.upper() for s in strings]
print(uppercase_strings)
