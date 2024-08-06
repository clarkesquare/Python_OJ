import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
scores = {}
subject = ""
tmp = 0
answer = [0, 0]

for _ in range(n):
    a, b = input().split()
    b = int(b.strip())
    scores[a] = b

for _ in range(k):
    subject = input().strip()
    tmp += scores[subject]
    del scores[subject]

scores = list(scores.items())
scores.sort(key = lambda x:x[1])

for i in range(m-k):
    answer[0] += scores[i][1]
    answer[1] += scores[i * -1 -1][1]

print(tmp+answer[0], tmp+answer[1])