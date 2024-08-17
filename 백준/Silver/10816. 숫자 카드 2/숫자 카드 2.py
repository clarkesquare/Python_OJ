import sys

input = sys.stdin.readline
pattern = {}
answer = []

n = int(input())
for i in map(int, input().split()):
    if i not in pattern:
        pattern[i] = 1
    
    else:
        pattern[i] += 1

m = int(input())
for j in map(int, input().split()):
    if j not in pattern:
        answer.append(0)
    
    else:
        answer.append(pattern[j])

print(*answer)