players = []
name = ""
n = 0

for _ in range(int(input())):
    players = list(input().split())
    name = input()
    n = int(input()) + players.index(name) - 1
    print(players[n%len(players)])