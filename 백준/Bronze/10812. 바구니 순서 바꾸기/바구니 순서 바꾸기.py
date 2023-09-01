n, m = map(int, input().split())
numbers = list(range(1, n+1))

for _ in range(m):
    i, j, k = map(int, input().split())
    numbers = numbers[:i-1:] + numbers[k-1:j:] + numbers[i-1:k-1:] + numbers[j::]

print(*numbers)