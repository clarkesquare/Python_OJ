n = int(input())

for i in range(n):
    scores = list(map(int, input().split()))
    scores.sort()
    print(int(sum(scores[1:4]))) if (scores[3] - scores[1]) < 4 else print('KIN')