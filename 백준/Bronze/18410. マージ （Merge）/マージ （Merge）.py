a, b = input().split()
numbers = []

for _ in range(2):
    numbers += list(map(int, input().split()))

numbers.sort()
print(*numbers, sep='\n')