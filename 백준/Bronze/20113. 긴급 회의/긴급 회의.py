players = [0] * int(input())
votes = map(int, input().split())

for i in votes:
    if i != 0:
        players[i-1] += 1

if players.count(max(players)) > 1:
    print('skipped')
else:
    print(players.index(max(players)) + 1)