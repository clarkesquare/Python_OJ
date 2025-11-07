n, m = map(int, input().split())
answer = 0

original = {}
for _ in range(n):
    a, b = input().split()
    original[a] = int(b)

for _ in range(m):
    a, b = input().split()
    b = int(b)
    if original[a] * 1.05 < b:
        answer += 1

print(answer)