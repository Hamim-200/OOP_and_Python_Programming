numbers = [45, 23, 21, 34, 56, 3, 2, 1, 98, 32]

# append(x)
numbers.append(100)
print("After appending 100:", numbers)

# insert(i, x)
numbers.insert(3, 99)
print("After inserting 99 at index 3:", numbers)

# pop([i])
popped = numbers.pop()
print("Popped element:", popped)
print("List after popping:", numbers)

# remove(x)
numbers.remove(99)
print("After removing 99:", numbers)

# index(x)
index_56 = numbers.index(56)
print("Index of 56:", index_56)

# count(x)
count_32 = numbers.count(32)
print("Count of 32:", count_32)

# sort()
numbers.sort()
print("Sorted list:", numbers)

# reverse()
numbers.reverse()
print("Reversed list:", numbers)

# copy()
numbers_copy = numbers.copy()
print("Copied list:", numbers_copy)

# clear()
numbers_copy.clear()
print("Cleared copy:", numbers_copy)


# After appending 100: [45, 23, 21, 34, 56, 3, 2, 1, 98, 32, 100]
# After inserting 99 at index 3: [45, 23, 21, 99, 34, 56, 3, 2, 1, 98, 32, 100]
# Popped element: 100
# List after popping: [45, 23, 21, 99, 34, 56, 3, 2, 1, 98, 32]
# After removing 99: [45, 23, 21, 34, 56, 3, 2, 1, 98, 32]
# Index of 56: 4
# Count of 32: 1
# Sorted list: [1, 2, 3, 21, 23, 32, 34, 45, 56, 98]
# Reversed list: [98, 56, 45, 34, 32, 23, 21, 3, 2, 1]
# Copied list: [98, 56, 45, 34, 32, 23, 21, 3, 2, 1]
# Cleared copy: []
