n, m = map(int, input().split())
numbers = []
i = 0

while len(numbers) < m:
    i += 1
    numbers += [i] * i

print(sum(numbers[n-1:m]))