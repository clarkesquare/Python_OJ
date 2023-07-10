import sys
input = sys.stdin.readline

scores = []

for i in range(int(input())):
    scores.append(list(input().split()))
    scores[i][1], scores[i][2], scores[i][3] = int(scores[i][1]), int(scores[i][2]), int(scores[i][3])

scores.sort(key=lambda x: x[0])
scores.sort(key=lambda x: x[3], reverse=True)
scores.sort(key=lambda x: x[2])
scores.sort(key=lambda x: x[1], reverse=True)

for j in scores:
    print(j[0])