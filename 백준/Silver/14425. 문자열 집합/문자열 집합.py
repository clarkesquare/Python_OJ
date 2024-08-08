import sys

input = sys.stdin.readline

n, m = map(int, input().split())
comparison = {}
answer = 0

for _ in range(n):
    comparison[input().strip()] = ""

for _ in range(m):
    if input().strip() in comparison:
        answer += 1

print(answer)