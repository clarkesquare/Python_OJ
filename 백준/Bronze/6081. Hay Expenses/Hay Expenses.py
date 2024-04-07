n, m = map(int, input().split())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

for _ in range(m):
    a, b = map(int, input().split())
    print(sum(numbers[a-1:b]))