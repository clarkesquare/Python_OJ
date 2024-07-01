import sys

input = sys.stdin.readline
answer = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    if abs(a - answer) <= b:
        answer += 1

print(answer)