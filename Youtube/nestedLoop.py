a = int(input("Enter a number:"))

if a < 10:
    if (a % 2) == 0:
        print('Less, Yes')
    else:
        print('Less, No')
else:
    if (a % 3) == 0:
        print('Greater, Yes')
    else:
        print('Greater, No')


# 1. User will enter a number, if the number is divisible by 3 and 5
#  the output will be yes otherwise output will be no.

number = int(input("Enter a number:"))

if number % 3 == 0 and number % 5 == 0:
    print('Yes The number is divisible by 3 and 5')
else:
    print('No The number is not divisible by 3 and 5')


# 2. User will enter a number, if the number is positive
# the output will be positive  otherwise output will be
# negative if the number is zero the output will be zero.

number = int(input("Enter a number:"))

if number > 0:
    print('Positive number')
elif number < 0:
    print('Negative Number')
else:
    print('Zero')

# 3. User will enter a number, if the number odd the
# output will be odd  otherwise output will be even

number = int(input("Enter a number:"))
if number % 2 == 0:
    print('Even Number')
else:
    print('Odd Number')

# 4. User will enter a character , if the character is vowel
# output will be vowel  otherwise output will be consonent and if the character does not fa;; within the alphabet the output will be nothing.

alphabet = input("Enter: ")

if alphabet >= 'a' and alphabet <= 'z' or alphabet >= 'A' and alphabet <= 'Z':
    if alphabet in 'aeiouAEIOU':
        print('Vowel')
    else:
        print('Consonent')
else:
    print('Nothing')
