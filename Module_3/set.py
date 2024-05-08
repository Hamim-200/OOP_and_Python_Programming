my_set = {1, 2, 3, 4, 5}
another_set = set([4, 5, 6, 7, 8])
my_set.add(6)


duplicate_set = {1, 2, 2, 3, 3, 4, 4, 5, 5}
print(duplicate_set)  # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # Union of set1 and set2
intersection_set = set1 & set2  # Intersection of set1 and set2
difference_set = set1 - set2  # Elements in set1 but not in set2

print(union_set)  # Output: {1, 2, 3, 4, 5}
print(intersection_set)  # Output: {3}
print(difference_set)  # Output: {1, 2}
