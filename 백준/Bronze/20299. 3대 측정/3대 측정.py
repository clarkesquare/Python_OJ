import sys

input = sys.stdin.readline
n, k, l = map(int, input().split())
answer = []
cnt = 0

for _ in range(n):
    team = list(map(int, input().split()))
    if sum(team) >= k and min(team) >= l:
        answer += team
        cnt += 1

print(cnt)
print(*answer)