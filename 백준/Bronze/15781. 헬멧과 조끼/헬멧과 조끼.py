a, b = map(int, input().split())
answer = 0

for _ in range(2):
    pattern = list(map(int, input().split()))
    answer += max(pattern)

print(answer)