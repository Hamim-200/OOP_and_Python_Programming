input_string = input()

left = 0
right = 0
current_string = ""
balanced_substrings = []

for char in input_string:
    if char == 'L':
        left =left+ 1
    else:
        right =right + 1

    current_string += char

    if left == right:
        balanced_substrings.append(current_string)
        current_string = ""
        left = 0
        right = 0

num_splits = len(balanced_substrings)

print(num_splits)

for substring in balanced_substrings:
    print(substring)
