n = int(input())
game = [[], [], []]
score = []

for _ in range(n):
    a, b, c = map(int, input().split())
    game[0].append(a)
    game[1].append(b)
    game[2].append(c)
    score.append(0)

for i in range(3):
    for j in range(n):
        if game[i].count(game[i][j]) == 1:
            score[j] += game[i][j]

for k in score:
    print(k)