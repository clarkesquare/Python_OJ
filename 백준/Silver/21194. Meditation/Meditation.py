n, m = map(int, input().split())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=True)
print(sum(numbers[:m]))