import sys

n = int(input())
score = []

for i in range(n):
    score.append(int(sys.stdin.readline()))

score = sorted(score)
        
for j in score:
    print(j)