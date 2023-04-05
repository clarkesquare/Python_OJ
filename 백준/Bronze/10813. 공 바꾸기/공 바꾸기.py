n, m = map(int, input().split())

numbers = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    numbers[i], numbers[j] = numbers[j], numbers[i]

print(*numbers)