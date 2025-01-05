n, x, k = map(int,input().split())
game = [0] * n
game[x-1] = 1

for _ in range(k):
    a, b = map(int, input().split())
    game[a-1], game[b-1] = game[b-1], game[a-1]

print(game.index(1)+1)