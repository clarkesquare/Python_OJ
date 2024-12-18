n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort()
print(*numbers, sep = "\n")