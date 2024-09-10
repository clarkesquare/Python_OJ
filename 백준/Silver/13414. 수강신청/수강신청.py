import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sugang = {}
answer = []

for _ in range(m):
    tmp = input().strip("\n")
    if tmp not in sugang:
        sugang[tmp] = ""
    
    else:
        sugang.pop(tmp)
        sugang[tmp] = ""

for k, v in sugang.items():
    answer.append(k)
    if len(answer) == n:
        break

print(*answer, sep="\n")