score1 = 0
score2 = 0
team1 = []
team2 = []
answer = 0

n = int(input())
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

for i in range(n):
    score1 += team1[i]
    score2 += team2[i]
    if score1 == score2:
        answer = i + 1

print(answer)