import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temp = []
answer = []

for _ in range(2):
    temp.append(map(int, input().split()))

for i in temp:
    answer += i

answer.sort()
print(*answer)