N = int(input())
sequence = list(map(int, input().split()))
removals = 0

count = {}
for num in sequence:
    count[num] = count.get(num, 0)

for num in sequence:
    count[num] += 1

for num, freq in count.items():
    if freq > num:
        removals += freq - num
    elif freq < num:
        removals += freq

print(removals)
