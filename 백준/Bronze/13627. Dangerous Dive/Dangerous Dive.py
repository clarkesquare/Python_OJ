n, m = map(int, input().split())
numbers = list(map(int, input().split()))

answer = []

for i in range(1, n+1):
    if i not in numbers:
        answer.append(i)

print(*answer if len(answer) != 0 else "*")