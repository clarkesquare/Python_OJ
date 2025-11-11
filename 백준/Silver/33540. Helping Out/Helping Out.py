import sys

input = sys.stdin.readline
scores = {}
answer = []

for _ in range(int(input())):
    a, b = input().split()
    scores[a] = scores.get(a, 0) + int(b)

answer = list(scores.items())
answer.sort(key= lambda x:x[0])
for i in answer:
    print(*i)