wins = []
score = []
n = 0
game = input()

while True:
    wins = []
    while True:
        if wins.count('A') == 21 or wins.count('B') == 21:
            break

        wins.append(game[n])
        n += 1
    
    print(str(wins.count('A')) + '-' + str(wins.count('B')))
    if wins.count('A') == 21:
        score.append('A')
    else:
        score.append('B')

    if score.count('A') == 2 or score.count('B') == 2:
        break

print('A' if score.count('A') > score.count('B') else 'B')