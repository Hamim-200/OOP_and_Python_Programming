name = 'Sakib\'s Khan' #Escape
name2 = "Sakib Khan"
name3 = """Sakib Khan
            number one

"""

print(name)
print(name2)
print(name3)
#String is a sequence of characters
for char in name2:
    print(char)
# Mutable means changabe
# Immutable means you can't change it

print(name2[3])
print(name[1:6])
print(name[-3])
print(name[::-1])

if 'Khan' in name2:
    print('Exists')

