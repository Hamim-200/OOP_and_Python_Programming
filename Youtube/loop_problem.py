# 1. A list of number from 1 to 100 that are divisible by 3 but not by 5 should be output

lst = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        lst.append(i)
print(lst)


# 2. Lets say there is a list of the different numbers. The list is as follows -
# 13, 23, 42, 42, 13, 24, 64, 65, 78, 578, 53, 24, 27, 98, 76, 55, 43, 32,
# 34, 55, 78, 89, 54, 23, 46, 54, 65, 45, 32, 57, 55, 46, 46 from this list
# a list of numbers less than 50 should be created and displayed as output

my_list = [13, 23, 42, 42, 13, 24, 64, 65, 78, 578, 53, 24, 27, 98, 76, 55, 43, 32,
           34, 55, 78, 89, 54, 23, 46, 54, 65, 45, 32, 57, 55, 46, 46]
for item in my_list:
    if item < 50:
        print(item)


# 3. Lets say there is a list of the different numbers. The list is as follows -
# 13, 23, 42, 42, 13, 24, 64, 65,34, 78, 78, 53, 24, 27, 98, 76, 55,
# 43, 32, 34, 55, 78, 89, 54, 23, 46, 54, 65, 45, 32, 57, 55, 46, 46
# from this list remove all the duplicta value

my_list = [13, 23, 42, 42, 13, 24, 64, 65, 34, 78, 78, 53, 24, 27, 98, 76, 55,
           43, 32, 34, 55, 78, 89, 54, 23, 46, 54, 65, 45, 32, 57, 55, 46, 46]

a = []

for items in my_list:
    if items not in a:
        a.append(items)
print(a)
