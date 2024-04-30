# PASSWORD GENERATOR

import string
import secrets

l = string.ascii_letters
d = string.digits
sc = string.punctuation

alphabet = l+d+sc

password_length = 8
temp = ""

for i in range(password_length):
    temp = temp + secrets.choice(alphabet)

print(temp)
