import sys

input = sys.stdin.readline

n = int(input())
players = {}
runner = ""
answer = []

for _ in range(n):
    runner = input().strip()
    if runner not in players:
        players[runner] = 1
    
    else:
        players[runner] += 1

for _ in range(n-1):
    runner = input().strip()
    if players[runner] == 1:
        del players[runner]

    else:
        players[runner] -= 1

answer = list(players.items())
print(answer[0][0])