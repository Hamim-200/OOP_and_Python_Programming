name = {'chando', 'mishu', 'chaity', 'shanto', 'jame', 'chando'}
print(name)

number = set({1, 2, 3, 4, 5, 6, 7, 8, 9})
print(number)

set1 = {1, 2, 3, 4}
set1.add(5)  # add an element to the set
set1.remove(4)  # remove an element from the set
print(set1)  # {1, 2, 3, 5}

a = set('1232681')
a = list(a)
a.sort()
print(a)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.union(set2)  # elements in either set1 or set2 ={1, 2, 3, 4, 5}
set1.intersection(set2)  # elements in both set1 and set2 ={3}
set1.difference(set2)  # elements in set1 but not in set2 ={1, 2}
