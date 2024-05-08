import math

print(math.sqrt(16))  # Output: 4.0
print(math.sin(math.pi/2))  # Output: 1.0
print(math.floor(4.6))  # Output: 4


import random

print(random.random())     # Random float between 0 and 1
print(random.randint(1, 100))  # Random integer between 1 and 100
print(random.choice(['apple', 'banana', 'grapes']))  # Random choice from a list


import time

print(time.time())  # Current time in seconds since the Epoch
time.sleep(2)       # Pause execution for 2 seconds
print(time.ctime()) # Current local time
