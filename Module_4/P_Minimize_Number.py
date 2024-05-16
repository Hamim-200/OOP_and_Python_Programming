N = int(input())
numbers = list(map(int, input().split()))

count = 0

while all(num % 2 == 0 for num in numbers):
    numbers = [num // 2 for num in numbers]
    count =count + 1

print(count)
